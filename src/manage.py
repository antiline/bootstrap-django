#!/usr/bin/env python

import os
import sys

from libs.secrets import Secrets
from libs.secrets.constants import SecretKey

if __name__ == "__main__":
    # copy system arguments
    arguments = sys.argv[:]
    setting_path = f'sites.settings.{Secrets.get(SecretKey.ENVIRONMENT)}'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting_path)
    from django.core.management import execute_from_command_line

    execute_from_command_line(arguments)
