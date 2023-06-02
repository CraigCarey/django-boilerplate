import pytest

from django.test import override_settings

SECRET_KEY_TEST_OVERRIDE = 'b27c612c6cbeac10c8788fbc95b29f563cc0ea2eb7d6be08'


# Automatically picked up across all tests
@pytest.fixture(autouse=True)
def test_settings(settings):
    with override_settings(SECRET_KEY=SECRET_KEY_TEST_OVERRIDE,):
        yield  # hands over to pytest
