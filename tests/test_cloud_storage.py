""" unit tests """
from unittest.mock import patch, MagicMock

import pytest
import requests


from ae.cloud_storage import DigiApi, GoodriveApi, csh_api_class


def test_csh_api_class():
    assert csh_api_class('Digi') is DigiApi
    assert csh_api_class('Goodrive') is GoodriveApi


@pytest.fixture
def digi_api():
    """ fully mocked DigiApi class instance. """
    with patch('ae.cloud_storage.requests.Session'):
        csh = DigiApi(root_folder="tst-root-folder", email="tst-email", password="tst-password")
        yield csh


@pytest.fixture
def digi_req_exc():
    """ raises exception in get/post requests (excluding the get request in DigiApi.__init__() to get token). """
    mock_session = MagicMock(spec=requests.Session())
    mock_session.post.side_effect = requests.exceptions.RequestException("tst-post-exception")
    with patch('ae.cloud_storage.requests.Session', return_value=mock_session):
        csh = DigiApi(root_folder="err-tst-root-folder", email="err-tst-email", password="err-tst-password")
        mock_session.get.side_effect = requests.exceptions.RequestException("tst-get-exception")
        yield csh


class TestDigiApi:
    def test___init(self, digi_api):
        assert isinstance(digi_api.session, MagicMock)
        assert isinstance(digi_api.error_message, str) and digi_api.error_message == ""
        assert isinstance(digi_api.base_url, str) and digi_api.base_url != ""
        assert isinstance(digi_api.files_mount_id, str) and digi_api.files_mount_id != ""
        assert isinstance(digi_api.root_folder, str) and digi_api.root_folder != ""

    def test___init_err(self, digi_req_exc):
        assert isinstance(digi_req_exc.session, MagicMock)
        assert isinstance(digi_req_exc.error_message, str) and digi_req_exc.error_message == ""
        assert isinstance(digi_req_exc.base_url, str) and digi_req_exc.base_url != ""
        assert isinstance(digi_req_exc.files_mount_id, str) and digi_req_exc.files_mount_id != ""
        assert isinstance(digi_req_exc.root_folder, str) and digi_req_exc.root_folder != ""

    def test___init_with_invalid_kwargs(self):
        with pytest.raises(AssertionError):
            DigiApi(unknown_kwarg="tst-invalid-kwarg")

    def test_delete_file_or_folder(self, digi_api):
        assert digi_api.delete_file_or_folder("tst-root-folder") == ""
        assert digi_api.error_message == ""

    def test_delete_file_or_folder_err(self, digi_req_exc):
        assert digi_req_exc.delete_file_or_folder("tst-root-folder") == ""
        assert digi_req_exc.error_message == ""

    def test_deployed_file_content(self, digi_api):
        assert digi_api.deployed_file_content("tst-file_path")

    def test_deployed_file_content_err(self, digi_req_exc):
        assert digi_req_exc.deployed_file_content("tst-file_path") is None

    def test_deploy_file_name_err(self, digi_api):
        fil_nam = ":invalid-file-name"
        assert digi_api.deploy_file(fil_nam) == ""
        assert "invalid character" in digi_api.error_message
        assert fil_nam in digi_api.error_message

    def test_deploy_file_not_exists_locally(self, digi_api):
        fil_nam = "tst-not-existing-file"
        assert digi_api.deploy_file(fil_nam) == ""
        assert "error reading" in digi_api.error_message
        assert fil_nam in digi_api.error_message

    def test_deploy_file_not_exists_remotely(self, digi_api):
        fil_nam = "requirements.txt"
        assert digi_api.deploy_file(fil_nam) == fil_nam
        assert digi_api.error_message == ""

        digi_api.list_dir = lambda _path: [fil_nam]
        assert digi_api.deploy_file(fil_nam) == fil_nam
        assert digi_api.error_message == ""

        digi_api.list_dir = lambda _path: None
        assert digi_api.deploy_file(fil_nam) == fil_nam
        assert digi_api.error_message == ""

        digi_api.list_dir = lambda _path: None
        digi_api._create_dirs = lambda _path: setattr(digi_api, 'error_message', "tst-err-msg")
        assert digi_api.deploy_file(fil_nam) == ""
        assert digi_api.error_message == "tst-err-msg"

    def test_list_dir(self, digi_api):
        assert digi_api.list_dir("tst-root-folder") == []
        assert digi_api.error_message == ""

    def test_list_dir_err(self, digi_req_exc):
        assert digi_req_exc.list_dir("tst-root-folder") is None
        assert 'tst-get-exception' in digi_req_exc.error_message

    def test_request_and_create_dirs_double_slash_err(self, digi_api):
        with patch('ae.cloud_storage.requests.Session.post', side_effect=Exception("tst-exception-on-session.post")):
            assert isinstance(digi_api.error_message, str)
            assert digi_api.error_message == ""                                    # err msg gets internally deleted

            # test error if root_folder contains 2 continuous slash chars
            csh = DigiApi(root_folder="tst // in root-folder", email="tst-email", password="tst-password")
            assert isinstance(csh.error_message, str) and csh.error_message == ""   # err msg gets internally deleted

    def test_request_and_create_dirs_double_slash_err2(self):
        with (patch('ae.cloud_storage.requests.Session'),
              patch('ae.cloud_storage.requests.Session.post', side_effect=Exception("tst-exception-on-session.post"))):
            csh = DigiApi(root_folder="tst // in root-folder", email="tst-email", password="tst-password")
            assert isinstance(csh.error_message, str) and csh.error_message == ""   # err msg gets internally deleted


@pytest.fixture
def goo_service():
    service = MagicMock()       # mock the chain: service.files().list().execute()
    return service


@pytest.fixture
def goo_api(goo_service):
    """ provides a GoodriveApi instance with all external dependencies patched out. """
    with (patch('ae.cloud_storage.build', return_value=goo_service),
          patch('ae.cloud_storage.service_account.Credentials.from_service_account_info'),
          patch('ae.cloud_storage.service_account.Credentials.from_service_account_file')):
        # We pass a dict to trigger the service account auth path
        api = GoodriveApi(sa_cred_dict={'tech': 'gemini'})
        yield api


class TestGoodriveApi:
    def test___init(self):
        with patch('ae.cloud_storage.build'):  # patch googleapiclient.discovery.build()
            goo_mock = GoodriveApi(root_folder="tst-root-folder")

            assert isinstance(goo_mock.root_folder_id_default, str) and goo_mock.root_folder_id_default != ""
            assert isinstance(goo_mock.error_message, str) and goo_mock.error_message == ""
            assert isinstance(goo_mock.service, MagicMock)

    def test_init_with_sa_file(self):
        with (patch('ae.cloud_storage.os_path_isfile', return_value=True) as _mock_isfile,
              patch('ae.cloud_storage.service_account.Credentials.from_service_account_file') as mock_cred,
              patch('ae.cloud_storage.build')):
            GoodriveApi(sa_cred_file='dummy.json')

            mock_cred.assert_called_once_with('dummy.json', scopes=['https://www.googleapis.com/auth/drive'])

    def test_request_exception(self, goo_api):
        mock_prepared_call = MagicMock()
        mock_prepared_call.execute.side_effect = Exception("tst-goo-api-exception")

        result = goo_api._request(mock_prepared_call)

        assert result == {}
        assert "HttpError" in goo_api.error_message

    @pytest.mark.parametrize("path, list_returns, expected_ids, expected_err", [
        # file found immediately
        ("file.txt", [{'files': [{'id': '123', 'mimeType': 'text/plain'}]}], ('root', '123'), ""),

        # path is a folder (trailing slash)
        ("folder/", [{'files': [{'id': 'f1', 'mimeType': GoodriveApi.FOLDER_MIMETYPE}]}], ('root', 'f1'), ""),

        # path item is a file, but more parts follow (error)
        ("file.txt/oops.txt", [{'files': [{'id': '123', 'mimeType': 'text/plain'}]}], ('root', ''),
         "is a file, not a folder"),

        # Google Documents warning
        ("my_doc", [{'files': [{'id': 'd1', 'mimeType': 'application/vnd.google-apps.doc'}]}], ('root', 'd1'),
         "Warning: Google Documents"),
    ])
    def test_folder_file_ids_scenarios(self, goo_api, path, list_returns, expected_ids, expected_err):
        with patch.object(goo_api, '_request', side_effect=list_returns):
            ids = goo_api.folder_file_ids(path)

            assert ids == expected_ids
            if expected_err:
                assert expected_err in goo_api.error_message

    def test_folder_file_ids_recursive_creation(self, goo_api):
        """ verify that folders are created if they don't exist and create_folders=True.
        * step 1: list 'sub' -> returns empty
        * step 2: _create_folder -> returns new folder id
        * step 3: list 'file.txt' -> returns file id
        """
        with (patch.object(goo_api, '_request') as mock_req,
              patch.object(goo_api, '_create_folder') as mock_create):
            mock_req.side_effect = [
                {'files': []},  # List 'sub'
                {'files': [{'id': 'file_id', 'mimeType': 'text/plain'}]}  # List 'file.txt'
            ]
            mock_create.return_value = {'id': 'sub_id', 'mimeType': goo_api.FOLDER_MIMETYPE}

            ids = goo_api.folder_file_ids("sub/file.txt", create_folders=True)

            assert ids == ('sub_id', 'file_id')
            mock_create.assert_called_once_with('sub', 'root')

    def test_deploy_file_update_existing_file(self, goo_api, goo_service):
        with (patch('ae.cloud_storage.MediaFileUpload'),
              patch.object(goo_api, 'folder_file_ids', return_value=('f_id', 'existing_id')),
              patch.object(goo_api, '_request', return_value={'id': 'existing_id'})):
            res = goo_api.deploy_file("test.txt")

            assert res == "existing_id"
            goo_service.files().update.assert_called()

    def test_deploy_file_invalid_chars_in_path(self, goo_api):
        res = goo_api.deploy_file("invalid:name.txt")

        assert res == ""
        assert "invalid character" in goo_api.error_message

    def test_delete_file_and_empty_trash(self, goo_api, goo_service):
        with (patch.object(goo_api, 'folder_file_ids', return_value=('f_id', 'target_id')),
              patch.object(goo_api, '_request', return_value={})):
            goo_api.delete_file_or_folder("path/to/delete", empty_trash=True)

            goo_service.files().delete.assert_called_with(fileId='target_id')
            goo_service.files().emptyTrash.assert_called()

    def test_deployed_file_content_chunk_download_success(self, goo_api):
        with (patch.object(goo_api, 'folder_file_ids', return_value=('f_id', 'target_id')),
              patch('ae.cloud_storage.MediaIoBaseDownload') as mock_dl_class):
            mock_dl_instance = mock_dl_class.return_value                               # configure downloader mock
            mock_dl_instance.next_chunk.side_effect = [(None, False), (None, True)]     # 1st: not done, 2nd call: done

            def fill_buffer(*_args, **_kwargs):                                         # mock data write to buffer
                mock_dl_class.call_args[0][0].write(b"content_bytes")                   # 1st arg is the BytesIO handle
                return None, True

            mock_dl_instance.next_chunk.side_effect = fill_buffer

            content = goo_api.deployed_file_content("file.txt")

            assert content == b"content_bytes"

    def test_wait_for_deployment_finish_polling(self, goo_api):
        with (patch.object(goo_api, 'folder_file_ids') as mock_ids,
              patch('time.time', side_effect=[100, 105])):  # mock start and end time

            mock_ids.side_effect = [('root', ''), ('root', ''), ('root', 'found_id')]   # 1st 2 tries return no file_id

            ids, tries, duration = goo_api.wait_for_deployment_finish("path", file_id="found_id")

            assert tries == 3
            assert ids[1] == "found_id"
            assert duration == 5
