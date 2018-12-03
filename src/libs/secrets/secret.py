import json

from libs.secrets.exceptions import ImproperlyConfigured


class Secrets:
    _secrets = None

    def __init__(self):
        self._load()

    def get(self, key: str) -> str:
        try:
            return self._secrets[key]

        except KeyError:
            raise ImproperlyConfigured('Set the {} environment variable!'.format(key))

    def _load(self) -> None:
        self._secrets = json.loads('')
