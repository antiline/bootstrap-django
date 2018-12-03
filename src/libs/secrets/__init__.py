import os

from libs.secrets.secret_handler import SecretHandler

# 파일 위치가 변경되면 아래 경로도 변경 해야 한다.
_root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../'))
Secrets = SecretHandler(_root_path)
