import os.path
from pathlib import Path

from split_settings.tools import include, optional

from core.general.utils.pytest import is_pytest_running

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namespacing our own custom environment variables
ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS_'

LOCAL_SETTINGS_PATH = os.getenv(f'{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH')

if not LOCAL_SETTINGS_PATH:
    # We dedicate local/settings.unittests.py to have reproducible unittest runs
    LOCAL_SETTINGS_PATH = (f'local/settings{".unittests" if is_pytest_running() else ".dev"}.py')

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

APPS_SETTINGS_PATH = f'{BASE_DIR}/core/apps/settings.py'

# These are the order that settings take precedence, e.g. settings in LOCAL_SETTINGS_PATH can override base
include(
    'base.py',
    'envvars.py',
    'logging.py',
    'custom.py',
    'docker.py',
    'db.py',
    optional(APPS_SETTINGS_PATH),
    optional(LOCAL_SETTINGS_PATH),
)

if not is_pytest_running():
    assert SECRET_KEY is not NotImplemented  # type: ignore # noqa: F821
