import os

from django.core.wsgi import get_wsgi_application

from libs.secrets import Secrets
from libs.secrets.constants import SecretKey

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'sites.settings.{Secrets.get(SecretKey.ENVIRONMENT)}')

application = get_wsgi_application()
