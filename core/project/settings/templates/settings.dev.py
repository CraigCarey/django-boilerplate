from django.contrib import messages

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4z-**pc=sf1qr6n7jjaitdu0gst$ch*5ra$ja7p*c_y^_g^w_p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

MESSAGE_LEVEL = messages.DEBUG

ALLOWED_HOSTS = ['*']

# Note: these only seem to apply to secondary included settings file, as in apps/settings.py
LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s'
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore
