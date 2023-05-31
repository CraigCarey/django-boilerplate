import pytest

from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from core.apps.accounts.models import User


@pytest.mark.django_db
# @freeze_time('2023-05-31')
def test_create_account(sender_account):
    user = User.objects.get(pk=sender_account.pk)

    assert user.email == 'test@test.com'
    assert user.invite_code == 'hula'

    assert user.date_joined.date() == timezone.now().date()
    assert not user.license_expired

    assert user.license_expiry == timezone.now().date() + timedelta(days=7)

    assert settings.SECRET_KEY == 'b27c612c6cbeac10c8788fbc95b29f563cc0ea2eb7d6be08'
