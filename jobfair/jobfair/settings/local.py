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

SECRET_KEY = 'i$cteu$9h8)l7_*_x8c$xt_q%$faa94-@-550)74ptsoo+2a0k'

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
