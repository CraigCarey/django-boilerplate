import pytest

from datetime import timedelta
from django.utils import timezone

from core.apps.accounts.models import User


@pytest.mark.django_db
# @freeze_time('2023-05-31')
def test_create_account(sender_account):
    user = User.objects.get(pk=sender_account.pk)

    assert user.email == 'test@test.com'
    assert user.invite_code == 'hula'

    assert user.date_joined.date() == timezone.now().date()
    assert not user.license_expired

    assert user.license_expiry

    # print(type(user.license_expiry))
    assert user.license_expiry == timezone.now().date() + timedelta(days=7)
