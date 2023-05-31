from datetime import timedelta

import django.dispatch
from django.db.models.signals import pre_save

from .models import User


@django.dispatch.receiver(pre_save, sender=User)
def set_default_user_license_expiry(sender, instance, *args, **kwargs):

    # if instance has not previously been saved
    if not instance.pk:
        instance.license_expiry = instance.date_joined + timedelta(days=7)
