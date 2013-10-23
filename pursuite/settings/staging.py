# -*- coding: utf-8 -*-
"""
    Setting for production env

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
#Flake8: noqa
from common import *

STATIC_ROOT = '/opt/pursuite/www/static'
MEDIA_ROOT = '/opt/pursuite/www/media'
ALLOWED_HOSTS = ['pursuite.openlabs.us']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pursuite_staging',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Email Settings
EMAIL_USE_TLS = False
EMAIL_HOST = 'mailtrap.io'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'nasscom-5ae7880ac967ae5d'
EMAIL_HOST_PASSWORD = 'eb5073db7bdb7af1'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

# Raven configuration
# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'http://e542381309e640bebb79ae26123e52e5:' + \
            '85869376ce9143a699ed05d07b552059@sentry.openlabs.co.in/22',
}
