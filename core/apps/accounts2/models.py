from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class AccountType(models.IntegerChoices):
        FREE = 1
        STANDARD = 2
        PROFESSIONAL = 3

    email = models.EmailField(unique=True)
    account_type = models.PositiveSmallIntegerField(choices=AccountType.choices, default=AccountType.FREE)
    date_of_birth = models.DateField(null=True)
    license_expiry = models.DateField(null=True)
    license_expired = models.BooleanField(default=False)
    invite_code = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'accounts2'


class Invite(models.Model):
    invite_code = models.CharField(max_length=128, unique=True)
    expiry = models.DateField()
    use_count = models.SmallIntegerField(default=0)
    use_limit = models.SmallIntegerField(default=1)
