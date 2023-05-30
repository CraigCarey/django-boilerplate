import pytest

from datetime import timedelta
from django.utils import timezone

from core.apps.accounts2.models import User

from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time('2023-05-30')
def test_create_account(sender_account):
    user = User.objects.get(pk=sender_account.pk)

    assert user.email == 'test@test.com'
    assert user.invite_code == 'hula'

    assert user.created_at.date() == timezone.now().date()
    assert user.license_expiry.date() == timezone.now().date() + timedelta(days=7)
    assert not user.license_expired
