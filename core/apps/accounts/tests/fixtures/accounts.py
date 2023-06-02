from datetime import datetime, timedelta

import pytest

from model_bakery import baker


@pytest.fixture
def sender_valid_invite_code():
    invite_code = 'valid'

    expiry = datetime.now() + timedelta(days=7)

    baker.make('accounts.Invite', invite_code=invite_code, expiry=expiry)

    return invite_code


@pytest.fixture
def sender_expired_invite_code():
    invite_code = 'expired'

    expiry = datetime.now() - timedelta(days=1)

    baker.make('accounts.Invite', invite_code=invite_code, expiry=expiry)

    return invite_code


@pytest.fixture
def sender_used_invite_code():
    invite_code = 'used'

    expiry = datetime.now() + timedelta(days=7)

    baker.make('accounts.Invite', invite_code=invite_code, expiry=expiry, use_count=1)

    return invite_code


@pytest.fixture
def sender_email():
    return 'test@test.com'


@pytest.fixture
def sender_username():
    return 'testuser12345'


@pytest.fixture
def sender_password():
    return '70bce3d1649c'


@pytest.fixture
def sender_account(sender_valid_invite_code, sender_email, db):
    print('sender_account...')
    return baker.make('accounts.User', email=sender_email, invite_code=sender_valid_invite_code)
