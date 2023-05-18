import os

from .misc import yaml_coerce


def get_settings_from_env(prefix):
    """
    'CORESETTINGS_IN_DOCKER=1'
    Becomes:
    {
        'IN_DOCKER': 1
    }
    """
    prefix_len = len(prefix)

    env_vars = os.environ.items()

    settings = {k[prefix_len:]: yaml_coerce(v) for k, v in env_vars if k.startswith(prefix)}

    return settings
