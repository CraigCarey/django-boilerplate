from core.project.settings.base import INSTALLED_APPS, TEMPLATES

INSTALLED_APPS += (
    'core.apps.accounts',
    'crispy_forms',
    'crispy_bootstrap5',
)

TEMPLATES[0]['DIRS'].append('core/apps/templates')  # type: ignore

AUTH_USER_MODEL = 'accounts.User'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

LOGOUT_REDIRECT_URL = '/'
