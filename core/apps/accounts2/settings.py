from core.project.settings.base import BASE_DIR, TEMPLATES

TEMPLATES[0]['DIRS'].append('core/apps/accounts2/templates')  # type: ignore

AUTH_USER_MODEL = 'accounts2.User'
AUTHENTICATION_BACKENDS = ('core.apps.accounts2.backends.EmailBackend',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
