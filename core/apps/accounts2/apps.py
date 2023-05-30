from django.apps import AppConfig


class Accounts2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.accounts2'

    def ready(self):
        pass
