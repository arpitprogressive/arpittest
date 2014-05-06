# -*- coding: utf-8 -*-
"""
    Setting for production env

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
#Flake8: noqa
import requests
from common import *
from django.conf import settings

STATIC_ROOT = '/opt/pursuite/www/static'
MEDIA_ROOT = '/opt/pursuite/www/media'
ALLOWED_HOSTS = ['www.sscnasscom.com', 'app.sscnasscom.com']

EC2_PRIVATE_IP  =   None
try:
    EC2_PRIVATE_IP  =   requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout = 0.01).text
except requests.exceptions.RequestException:
    pass

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pursuite',
        'USER': 'masteruser',
        'PASSWORD': 'masterpassword',
        'HOST': 'pursuite.cghk8zawexlj.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

# Email Settings
DEFAULT_FROM_EMAIL = 'no-reply@sscnasscom.com'
EMAIL_SUBJECT_PREFIX = '[SSC-NASSCOM] '
EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'AKIAIUWKC7L5IYUUZ45A'
EMAIL_HOST_PASSWORD = 'Ai9KREEHk93RbZ1xAbOJBonTgCJd4/QiWMEkoImF/SBT'

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
    'dsn': 'http://c832ebf4689e40c8a6585e65299830df:'
           '560dbc317d78408ea995b0f84ed68ad6@sentry.openlabs.co.in/32',
}

# Add amazon s3 as a storage mechanism
INSTALLED_APPS += ('storages', 's3_folder_storage',)
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
#STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = "static"

AWS_ACCESS_KEY_ID = "AKIAIT5S5O6FUGYEAO5Q"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "pursuite-production"
AWS_QUERYSTRING_AUTH = False

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//d3ehxvmjnyu31p.cloudfront.net/media/'    # CDN
#STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//d3ehxvmjnyu31p.cloudfront.net/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Setup caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': 'pursuite.vbzolj.cfg.apse1.cache.amazonaws.com:11211',
    }
}

# Setup elastic search connection
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://search.sscnasscom.com:9200/',
        'INDEX_NAME': 'haystack',
    },
}
