from libs.base.constants import BaseConstant

SECRET_FILE_NAME = 'secrets.json'


class SecretEnvironment(BaseConstant):
    DEV = 'development'
    STAGING = 'staging'
    PROD = 'production'

    _LIST = (DEV, STAGING, PROD,)
    _STRING_MAP = {
        DEV: 'dev',
        STAGING: 'staging',
        PROD: 'prod'
    }


class SecretKey(BaseConstant):
    ENVIRONMENT = 'environment'

    SECRET_KEY = 'secret_key'

    _LIST = (ENVIRONMENT, SECRET_KEY,)
    _STRING_MAP = {
        ENVIRONMENT: 'environment',
        SECRET_KEY: 'django secret_key'
    }
