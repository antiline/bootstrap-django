import json
import os

from libs.secrets.constants import SECRET_FILE_NAME
from libs.secrets.exceptions import ImproperlyConfigured


class SecretHandler:
    def __init__(self, root_path: str):
        self._root_path = root_path
        self._secrets = {}
        self._load()

    def get(self, key: str) -> str:
        try:
            return self._secrets[key]

        except KeyError:
            raise ImproperlyConfigured('Set the {} environment variable!'.format(key))

    def _load(self) -> None:
        file_path = os.path.join(self._root_path, SECRET_FILE_NAME)
        self._secrets = json.loads(self._file_load(file_path))

    @staticmethod
    def _file_load(file_path: str):
        try:
            with open(file_path) as file:
                return file.read()

        except (OSError, IOError):
            raise ImproperlyConfigured('There is no setting file %s' % file_path)
