"""
Debug settings for the project.

These settings complement (and override) those in ``settings.py``.
To use run the server with:
``./manage.py runserver --settings settings_debug``

"""

# Load settings first
try:
    from settings import *
except ImportError:
    pass

# Now override any of them
DEBUG = True
TEMPLATE_DEBUG = DEBUG
LOG_LEVEL = 'DEBUG'
INTERNAL_IPS = ('127.0.0.1',)

#MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
INSTALLED_APPS += [#'debug_toolbar',    # Useful but a tad heavy.
                   'django_extensions',]
