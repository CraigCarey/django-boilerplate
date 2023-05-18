from .utils.collections import deep_update
from .utils.settings import get_settings_from_env
"""
This takes env variables with a matching prefix, strips out the prefix, and adds itto global settings

For example:
    export CORESETTINGS_IN_DOCKER=true (environment variable)

Could then be referenced as a global as:
    IN_DOCKER (where the value would be true)
"""

# globals() is a dictionary of global variables
# type ignore tells the IDE to ignore a non-error
deep_update(globals(), get_settings_from_env(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
