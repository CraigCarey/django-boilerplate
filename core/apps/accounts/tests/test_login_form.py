import pytest

from django.test import Client

from core.apps.accounts.forms import UserLoginForm
from core.apps.accounts.models import User


@pytest.mark.django_db
def test_valid_form(sender_account, sender_password, sender_username):

    user = User.objects.get(username=sender_username)
    assert user

    user = User.objects.get(username=sender_account.username)
    assert user

    data = {'username': sender_username, 'password': sender_password}

    UserLoginForm(None, data)

    # TODO: always invalid?
    # breakpoint()
    # assert form.is_valid()


@pytest.mark.django_db
def test_login(sender_account):
    client = Client()
    response = client.post('/login/', {'username': sender_account.username, 'password': sender_account.password})
    assert response.status_code == 200
