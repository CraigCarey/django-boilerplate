import logging

from django.conf import settings

from core.project.settings.base import INSTALLED_APPS, TEMPLATES

from split_settings.tools import include, optional

INSTALLED_APPS += (
    'crispy_forms',
    'crispy_bootstrap5',
)

CUSTOM_APPS = ('accounts', 'articles')

for a in CUSTOM_APPS:
    INSTALLED_APPS.append(f'core.apps.{a}')

    # Include app-specific settings (where they exist)
    include(optional(f'{a}/settings.py'))

TEMPLATES[0]['DIRS'].append('core/apps/templates')  # type: ignore

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

LOGOUT_REDIRECT_URL = '/'

logger = logging.getLogger(__name__)
logger.debug('DB Config:\n' f'{settings.DATABASES}')
