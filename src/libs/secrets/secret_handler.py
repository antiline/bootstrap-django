import json
import os

from libs.secrets.constants import SECRET_FILE_NAME
from libs.secrets.exceptions import ImproperlyConfigured


class SecretHandler:
    _instance = None

    def __init__(self):
        self._root_path = self._get_root_path()
        self._secrets = {}
        self._load()

    @classmethod
    def instance(cls) -> 'SecretHandler':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @staticmethod
    def _get_root_path() -> str:
        # 파일 위치가 변경되면 아래 경로도 변경 해야 한다.
        return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../'))

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
