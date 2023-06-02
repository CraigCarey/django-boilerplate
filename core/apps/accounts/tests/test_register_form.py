import pytest

from core.apps.accounts.forms import UserRegistrationForm
from core.apps.accounts.models import User


@pytest.mark.django_db
def test_valid_form(sender_valid_invite_code, sender_password, sender_email, sender_username):
    data = {
        'username': sender_username,
        'email': sender_email,
        'invite_code': sender_valid_invite_code,
        'account_type': 1,
        'password1': sender_password,
        'password2': sender_password,
    }

    form = UserRegistrationForm(data)

    assert form.is_valid()

    form.save()

    user = User.objects.get(username=sender_username)
    assert user.email == sender_email
    assert user.invite_code == sender_valid_invite_code
    assert user.account_type == 1


@pytest.mark.django_db
def test_invalid_invite(sender_password, sender_email, sender_username):

    invalid_invite_code = 'invalid'
    data = {
        'username': sender_username,
        'email': sender_email,
        'invite_code': invalid_invite_code,
        'password1': sender_password,
        'password2': sender_password,
    }

    form = UserRegistrationForm(data)

    assert not form.is_valid()

    assert len(form.errors) == 1
    assert len(form.errors['invite_code']) == 1

    assert form.errors['invite_code'][0] == f'"{invalid_invite_code}" is not a valid invite code'


@pytest.mark.django_db
def test_expired_invite(sender_expired_invite_code, sender_password, sender_email, sender_username):

    data = {
        'username': sender_username,
        'email': sender_email,
        'invite_code': sender_expired_invite_code,
        'password1': sender_password,
        'password2': sender_password,
    }

    form = UserRegistrationForm(data)

    assert not form.is_valid()

    assert len(form.errors) == 1
    assert len(form.errors['invite_code']) == 1

    assert form.errors['invite_code'][0] == f'Invite code "{sender_expired_invite_code}" has expired'


@pytest.mark.django_db
def test_used_invite(sender_used_invite_code, sender_password, sender_email, sender_username):

    data = {
        'username': sender_username,
        'email': sender_email,
        'invite_code': sender_used_invite_code,
        'password1': sender_password,
        'password2': sender_password,
    }

    form = UserRegistrationForm(data)

    assert not form.is_valid()

    assert len(form.errors) == 1
    assert len(form.errors['invite_code']) == 1
    assert form.errors['invite_code'][0] == f'Invite code "{sender_used_invite_code}" has reached use limit'
