import os

# Set on the earliest possible moment
os.environ['PYTEST_RUNNING'] = 'true'

from accounts2.tests.fixtures import *  # noqa: F401, F403, E402
