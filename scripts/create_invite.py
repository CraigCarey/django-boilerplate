#! /usr/bin/env python3

from datetime import datetime, timedelta

from core.apps.accounts.models import Invite

Invite.objects.all().delete()

yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

Invite(invite_code='ok', expiry=tomorrow).save()
Invite(invite_code='expired', expiry=yesterday).save()
Invite(invite_code='used', expiry=tomorrow, use_count=1).save()

invites = Invite.objects.all()
# invite = Invite.objects.get(invite_code="ok")

for invite in invites:
    print(f'\ninvite_code: {invite.invite_code}')
    print(f'expiry: {invite.expiry}')
    print(f'use_limit: {invite.use_limit}')
    print(f'use_count: {invite.use_count}')
