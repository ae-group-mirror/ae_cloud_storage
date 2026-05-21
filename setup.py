# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.78
""" setup of ae namespace module portion cloud_storage: distribute files to and retrieve them from cloud storage hosts.. """
import sys
# noinspection PyUnresolvedReferences
import pathlib
# noinspection PyUnresolvedReferences
import setuptools


print("SetUp " + __name__ + ": " + sys.executable + str(sys.argv) + f" {sys.path=}")

setup_kwargs = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    'description': 'ae namespace module portion cloud_storage: distribute files to and retrieve them from cloud storage hosts.',
    'extras_require': {
        'dev': [
            'aedev_project_tpls',
            'ae_ae',
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
        'docs': [],
        'tests': [
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
    },
    'install_requires': [
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'google-api-python-client',
        'requests',
        'types-requests',
        'ae_base',
        'ae_app_log',
        'ae_system',
    ],
    'keywords': [
        'configuration',
        'development',
        'environment',
        'productivity',
    ],
    'license': 'GPL-3.0-or-later',
    'long_description': (pathlib.Path(__file__).parent / 'README.md').read_text(encoding='utf-8'),
    'long_description_content_type': 'text/markdown',
    'name': 'ae_cloud_storage',
    'package_data': {
        '': [],
    },
    'packages': [
        'ae',
    ],
    'project_urls': {
        'Bug Tracker': 'https://gitlab.com/ae-group/ae_cloud_storage/-/issues',
        'Documentation': 'https://ae.readthedocs.io/en/latest/_autosummary/ae.cloud_storage.html',
        'Repository': 'https://gitlab.com/ae-group/ae_cloud_storage',
        'Source': 'https://ae.readthedocs.io/en/latest/_modules/ae/cloud_storage.html',
    },
    'python_requires': '>=3.12',
    'url': 'https://gitlab.com/ae-group/ae_cloud_storage',
    'version': '0.3.12',
    'zip_safe': True,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass
