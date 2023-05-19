from django.contrib import admin

from .models import Invite, User

admin.site.register(User)
admin.site.register(Invite)
