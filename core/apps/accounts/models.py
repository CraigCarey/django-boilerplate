from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in
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

    class Meta:
        app_label = 'accounts'


class Invite(models.Model):
    invite_code = models.CharField(max_length=128, unique=True)
    expiry = models.DateField()
    use_count = models.SmallIntegerField(default=0)
    use_limit = models.SmallIntegerField(default=1)


def check_license(user):

    if user.is_anonymous is False and user.is_superuser is False:
        expiry_date = user.license_expiry
        todays_date = datetime.today().date()

        if todays_date > expiry_date:
            user.license_expired = True
            user.save()


# Signals
def _check_license_handler(sender, user, request, **kwargs):
    check_license(user)


user_logged_in.connect(_check_license_handler)
