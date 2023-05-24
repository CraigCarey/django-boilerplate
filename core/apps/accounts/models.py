from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
import django.dispatch


# Create your models here.
class User(AbstractUser):

    class AccountType(models.IntegerChoices):
        FREE = 1
        STANDARD = 2
        PROFESSIONAL = 3

    account_type = models.PositiveSmallIntegerField(choices=AccountType.choices, default=AccountType.FREE)
    date_of_birth = models.DateField(null=True)
    license_expiry = models.DateField(null=True)
    license_expired = models.BooleanField(default=False)
    invite_code = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'accounts'


@django.dispatch.receiver(models.signals.post_init, sender=User)
def set_default_user_license_expiry(sender, instance, *args, **kwargs):

    if instance.created_at:
        instance.license_expiry = instance.created_at + timedelta(days=7)
        instance.save()


class Invite(models.Model):
    invite_code = models.CharField(max_length=128, unique=True)
    expiry = models.DateField()
    use_count = models.SmallIntegerField(default=0)
    use_limit = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
