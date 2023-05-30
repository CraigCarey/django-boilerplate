from datetime import timedelta
from django.utils import timezone

import django.dispatch
from django.db import models

from .models import User


@django.dispatch.receiver(models.signals.post_init, sender=User)
def set_default_user_license_expiry(sender, instance, *args, **kwargs):

    instance.created_at = timezone.now()
    instance.license_expiry = instance.created_at + timedelta(days=7)
    instance.save()
