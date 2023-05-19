from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    class AccountType(models.IntegerChoices):
        FREE = 1
        STANDARD = 2
        PROFESSIONAL = 3

    account_type = models.PositiveSmallIntegerField(choices=AccountType.choices)
    date_of_birth = models.DateField()
    license_expiry = models.DateField(default=datetime.now() + timedelta(days=7))
    license_expired = models.BooleanField(default=False)
    invite_code = models.CharField(max_length=128, null=True)

    class Meta:
        app_label = 'accounts'


class Invite(models.Model):
    invite_code = models.CharField(max_length=128, unique=True)
    expiry = models.DateField(default=datetime.now() + timedelta(days=7))
    use_count = models.SmallIntegerField(default=0)
    use_limit = models.SmallIntegerField(default=1)
