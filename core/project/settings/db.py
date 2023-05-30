from django.conf import settings

if not settings.DATABASES:
    if settings.DB_MODE == 'sqlite':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        }
    elif settings.DB_MODE == 'postgres':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'django_core',
                'USER': 'django_core',
                'PASSWORD': 'django_core',
                'HOST': 'localhost',
                'PORT': '5432',
                'ATOMIC_REQUESTS': True,  # type: ignore
                # TODO(dmu) MEDIUM:
                #   Unfortunately Daphne / ASGI / Django Channels do not properly reuse database connections
                #   and therefore we are getting resource (connection) leak that leads to the following:
                #   django.db.utils.OperationalError: FATAL:  sorry, too many clients already
                #   `'CONN_MAX_AGE': 0` is used as workaround. In case it notably affects performance
                #   implement a solution that either closes database connections on WebSocket client
                #   disconnect and implement connection pooling outside Django (BgBouncer or similar)
                'CONN_MAX_AGE': 0,  # type: ignore
            }
        }
    else:
        raise NotImplementedError(f'{settings.DB_MODE} not configured')
