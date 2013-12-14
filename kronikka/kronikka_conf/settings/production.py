from base import *

DEBUG = False

STATIC_ROOT = '/var/www/kronikat/static'

MEDIA_ROOT = '/var/www/kronikat/media'

ALLOWED_HOSTS = ['kronikat.hippuu.fi']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/var/www/kronikat/db.sqlite',             # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
