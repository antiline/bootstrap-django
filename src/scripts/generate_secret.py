import argparse
import os

from libs.secrets.constants import SECRET_FILE_NAME
from libs.secrets.secret_generator import SecretGenerator
from libs.secrets.secret_loader import JsonFileSecretLoader

# 스크림트 위치가 변경된다면 아래 ROOT_PATH 계산을 변경해야한다.
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
DEFAULT_DEV_FILE_PATH = os.path.join(ROOT_PATH, f'docs/dev/settings/{SECRET_FILE_NAME}')

args_parser = argparse.ArgumentParser()
args_parser.add_argument('-a', '--action', help='default')
args = args_parser.parse_args()

if args.action == 'default':
    SecretGenerator(ROOT_PATH, JsonFileSecretLoader(DEFAULT_DEV_FILE_PATH)).generate()

else:
    args_parser.print_help()
