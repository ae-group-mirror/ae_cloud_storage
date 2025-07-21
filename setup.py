# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.tpl_project V0.3.36
""" setup of ae namespace module portion cloud_storage: distribute files to and retrieve them from cloud storage hosts.. """



# noinspection PyUnresolvedReferences
import setuptools

setup_kwargs = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': ['Development Status :: 3 - Alpha', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', 'Natural Language :: English', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.9', 'Topic :: Software Development :: Libraries :: Python Modules'],
    'description': 'ae namespace module portion cloud_storage: distribute files to and retrieve them from cloud storage hosts.',
    'extras_require': {'dev': ['aedev_tpl_project', 'ae_ae', 'anybadge', 'coverage-badge', 'aedev_git_repo_manager', 'flake8', 'mypy', 'pylint', 'pytest', 'pytest-cov', 'pytest-django', 'typing', 'types-setuptools', 'wheel', 'twine'], 'docs': [], 'tests': ['anybadge', 'coverage-badge', 'aedev_git_repo_manager', 'flake8', 'mypy', 'pylint', 'pytest', 'pytest-cov', 'pytest-django', 'typing', 'types-setuptools', 'wheel', 'twine']},
    'install_requires': ['google-auth-oauthlib', 'google-auth-httplib2', 'google-api-python-client', 'requests', 'ae_base'],
    'keywords': ['configuration', 'development', 'environment', 'productivity'],
    'license': 'OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'long_description': '<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project ae.ae V0.3.96 -->\n<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.tpl_namespace_root V0.3.14 -->\n# cloud_storage 0.3.8\n\n[![GitLab develop](https://img.shields.io/gitlab/pipeline/ae-group/ae_cloud_storage/develop?logo=python)](\n    https://gitlab.com/ae-group/ae_cloud_storage)\n[![LatestPyPIrelease](\n    https://img.shields.io/gitlab/pipeline/ae-group/ae_cloud_storage/release0.3.7?logo=python)](\n    https://gitlab.com/ae-group/ae_cloud_storage/-/tree/release0.3.7)\n[![PyPIVersions](https://img.shields.io/pypi/v/ae_cloud_storage)](\n    https://pypi.org/project/ae-cloud-storage/#history)\n\n>ae namespace module portion cloud_storage: distribute files to and retrieve them from cloud storage hosts..\n\n[![Coverage](https://ae-group.gitlab.io/ae_cloud_storage/coverage.svg)](\n    https://ae-group.gitlab.io/ae_cloud_storage/coverage/index.html)\n[![MyPyPrecision](https://ae-group.gitlab.io/ae_cloud_storage/mypy.svg)](\n    https://ae-group.gitlab.io/ae_cloud_storage/lineprecision.txt)\n[![PyLintScore](https://ae-group.gitlab.io/ae_cloud_storage/pylint.svg)](\n    https://ae-group.gitlab.io/ae_cloud_storage/pylint.log)\n\n[![PyPIImplementation](https://img.shields.io/pypi/implementation/ae_cloud_storage)](\n    https://gitlab.com/ae-group/ae_cloud_storage/)\n[![PyPIPyVersions](https://img.shields.io/pypi/pyversions/ae_cloud_storage)](\n    https://gitlab.com/ae-group/ae_cloud_storage/)\n[![PyPIWheel](https://img.shields.io/pypi/wheel/ae_cloud_storage)](\n    https://gitlab.com/ae-group/ae_cloud_storage/)\n[![PyPIFormat](https://img.shields.io/pypi/format/ae_cloud_storage)](\n    https://pypi.org/project/ae-cloud-storage/)\n[![PyPILicense](https://img.shields.io/pypi/l/ae_cloud_storage)](\n    https://gitlab.com/ae-group/ae_cloud_storage/-/blob/develop/LICENSE.md)\n[![PyPIStatus](https://img.shields.io/pypi/status/ae_cloud_storage)](\n    https://libraries.io/pypi/ae-cloud-storage)\n[![PyPIDownloads](https://img.shields.io/pypi/dm/ae_cloud_storage)](\n    https://pypi.org/project/ae-cloud-storage/#files)\n\n\n## installation\n\n\nexecute the following command to install the\nae.cloud_storage module\nin the currently active virtual environment:\n \n```shell script\npip install ae-cloud-storage\n```\n\nif you want to contribute to this portion then first fork\n[the ae_cloud_storage repository at GitLab](\nhttps://gitlab.com/ae-group/ae_cloud_storage "ae.cloud_storage code repository").\nafter that pull it to your machine and finally execute the\nfollowing command in the root folder of this repository\n(ae_cloud_storage):\n\n```shell script\npip install -e .[dev]\n```\n\nthe last command will install this module portion, along with the tools you need\nto develop and run tests or to extend the portion documentation. to contribute only to the unit tests or to the\ndocumentation of this portion, replace the setup extras key `dev` in the above command with `tests` or `docs`\nrespectively.\n\nmore detailed explanations on how to contribute to this project\n[are available here](\nhttps://gitlab.com/ae-group/ae_cloud_storage/-/blob/develop/CONTRIBUTING.rst)\n\n\n## namespace portion documentation\n\ninformation on the features and usage of this portion are available at\n[ReadTheDocs](\nhttps://ae.readthedocs.io/en/latest/_autosummary/ae.cloud_storage.html\n"ae_cloud_storage documentation").\n',
    'long_description_content_type': 'text/markdown',
    'name': 'ae_cloud_storage',
    'package_data': {'': []},
    'packages': ['ae'],
    'project_urls': {'Bug Tracker': 'https://gitlab.com/ae-group/ae_cloud_storage/-/issues', 'Documentation': 'https://ae.readthedocs.io/en/latest/_autosummary/ae.cloud_storage.html', 'Repository': 'https://gitlab.com/ae-group/ae_cloud_storage', 'Source': 'https://ae.readthedocs.io/en/latest/_modules/ae/cloud_storage.html'},
    'python_requires': '>=3.9',
    'setup_requires': ['aedev_setup_project'],
    'url': 'https://gitlab.com/ae-group/ae_cloud_storage',
    'version': '0.3.8',
    'zip_safe': True,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass
