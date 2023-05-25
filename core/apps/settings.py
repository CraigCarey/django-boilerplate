from core.project.settings.base import INSTALLED_APPS, TEMPLATES

INSTALLED_APPS += (
    'crispy_forms',
    'crispy_bootstrap5',
)

CUSTOM_APPS = ('accounts2', 'articles')

for a in CUSTOM_APPS:
    INSTALLED_APPS.append(f'core.apps.{a}')

TEMPLATES[0]['DIRS'].append('core/apps/templates')  # type: ignore

# TODO: move into accounts2 settings?
AUTH_USER_MODEL = 'accounts2.User'
AUTHENTICATION_BACKENDS = ('core.apps.accounts2.backends.EmailBackend',)

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

LOGOUT_REDIRECT_URL = '/'
