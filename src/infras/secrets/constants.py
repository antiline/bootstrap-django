from libs.base.constants import BaseConstant

SECRET_FILE_NAME = 'secrets.json'

SECRET_FILE_CRYPTO_KEY_ENV_NAME = 'SECRET_FILE_CRYPTO_KEY'
DEFAULT_SECRET_FILE_CRYPTO_KEY = 'kn-ymMvrxZWjFrFMmZELqcA9b-BuGPW)'


class SecretEnvironment(BaseConstant):
    DEV = 'development'
    STAGING = 'staging'
    PROD = 'production'

    _LIST = (DEV, STAGING, PROD,)
    _STRING_MAP = {
        DEV: 'development',
        STAGING: 'staging',
        PROD: 'production'
    }


class SecretKey(BaseConstant):
    ENVIRONMENT = 'environment'

    SECRET_KEY = 'secret_key'

    _LIST = (ENVIRONMENT, SECRET_KEY,)
    _STRING_MAP = {
        ENVIRONMENT: 'environment',
        SECRET_KEY: 'django secret_key'
    }
