from .base import *

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions'
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}

ENVIRONMENT = 'local'
