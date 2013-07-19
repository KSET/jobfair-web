from os.path import abspath, join, dirname
import os
from django.core.exceptions import ImproperlyConfigured

PROJECT_DIR = abspath(join(dirname(__file__), '..'))

ADMINS = (
    ('Tomislav Maricevic', 'tmarice@kset.org'),
    ('Dino Lukman', 'grayfox@kset.org'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Zagreb'

LANGUAGE_CODE = 'hr-hr'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROOT_URLCONF = 'jobfair.urls'

STATIC_ROOT = join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    join(PROJECT_DIR, 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'south',

    'news',
    'cv',
    'media',
    'archive',
    'partners',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


WSGI_APPLICATION = 'jobfair.wsgi.application'
