from .base import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jobfair',  
        'USER': 'jobfair',
        'PASSWORD': 'jobfair',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
