import logging

from core.project.settings.base import BASE_DIR, TEMPLATES
from django.conf import settings

TEMPLATES[0]['DIRS'].append('core/apps/accounts2/templates')  # type: ignore

AUTH_USER_MODEL = 'accounts2.User'
AUTHENTICATION_BACKENDS = ('core.apps.accounts2.backends.EmailBackend',)

try:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'mitb.anyvision.it'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = settings.HOST_EMAIL_ADDRESS
    EMAIL_HOST_PASSWORD = settings.HOST_EMAIL_PASSWORD
    DEFAULT_FROM_EMAIL = 'sdkdemo@anyvision.it'
except AttributeError:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

    logger = logging.getLogger(__name__)
    logger.info(
        'SMTP not configured, did you set the following env variables?\n'
        ' - HOST_EMAIL_ADDRESS\n'
        ' - HOST_EMAIL_PASSWORD\n'
        f'  Using file based email backend instead ({EMAIL_FILE_PATH})\n'
    )

PASSWORD_RESET_TIMEOUT = 14400  # 4hrs
