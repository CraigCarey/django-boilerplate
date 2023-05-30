# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f-m_!kq_(jwcgs%i%t0+36i9flo+_h4j1^t$d&)+jr4m%m%5+b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Note: these only seem to apply to secondary included settings file, as in apps/settings.py
LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s'
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore
