from datetime import datetime, timedelta

import pytest

from model_bakery import baker


@pytest.fixture
def sender_invite_code():
    invite_code = 'hula'

    expiry = datetime.now() + timedelta(days=7)

    baker.make('accounts.Invite', invite_code=invite_code, expiry=expiry)

    return invite_code


@pytest.fixture
def sender_email():
    return 'test@test.com'


@pytest.fixture
def sender_account(sender_invite_code, sender_email, db):
    print('sender_account...')
    return baker.make('accounts.User', email=sender_email, invite_code=sender_invite_code)
