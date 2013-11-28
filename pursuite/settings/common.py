# -*- coding: utf-8 -*-
"""
    Common Settings

    These setting are common to all dev, prod, test enviornment

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
# Flake8: noqa
import os
PROJECT_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../"))
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_PATH + "/pursuite/web/media/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + "/pursuite/web/static/",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't%^ac6&lrkm-=+b&+)wb_q0kjzj=ia7c#fyqgn%6p8fs)4cqwb'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = {
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # allauth specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = 'pursuite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pursuite.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    #   "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + "/pursuite/web/templates/",
)

INSTALLED_APPS = (
    'admin',
    'account',
    'tinymce',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'haystack',
    'cmsindex',
    'analytics',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.teaser',
    'cms.plugins.video',
    'cms.plugins.text',
    'django.contrib.auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.twitter',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangocms_admin_style',
    'django.contrib.admin',
    'raven.contrib.django.raven_compat',
    'south',
    'pagination',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

CMS_TEMPLATES = (
    ('home.html', 'Home'),
    ('admin/qualification_packs.html', 'List Qualification Packs'),
    ('admin/occupational_standards.html', 'List Occupational Standards'),
    ('contact.html', 'Contact'),
    ('india-map.html', 'India Map'),
    ('supply.html', 'Analytics Supply'),
    ('demand.html', 'Analytics Demand'),
    ('article.html', 'Article'),
    ('news.html', 'News'),
    ('stakeholders.html', 'Stakeholders'),
    ('stakeholders-inner.html', 'Stakeholders Inner'),
    ('inner-article.html', 'Inner Article'),
    ('inner-article-with-box.html', 'Inner Article With Box'),
    ('common_blocks.html', 'Common Blocks'),
    ('wfmis.html', 'WFMIS'),
)
CMS_REDIRECTS = True

CMS_PLACEHOLDER_CONF = {
    'training-providers-footer-ad': {
        "plugins": ['PicturePlugin',]
    },
    'company-footer-ad': {
        "plugins": ['PicturePlugin',]
    },
    'institution-footer-ad': {
        "plugins": ['PicturePlugin',]
    },
}

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'theme_advanced_toolbar_location' : "top",
    'plugins': "table,spellchecker,contextmenu",
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,separator,\
        styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "cut,copy,paste,separator,bullist,numlist,\
        separator,outdent,indent,blockquote,separator,undo,redo,separator,\
        table,link,unlink,anchor,image,code,separator,forecolor,backcolor,\
        separator,hr,removeformat,separator,charmap,fullscreen,separator,\
        spellchecker",
    'width': 900,
    'height': 300,
    'resize': "both",
    'contextmenu': "link image inserttable | cell row column deletetable",
    'style_formats' : [
      {'title' : 'Button', 'selector' : 'a', 'classes' : 'btn btn-theme'},
    ],
}

LANGUAGES = [
    ('en', 'English'),
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

# CMS Permission
CMS_PERMISSION = True

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = 0
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# django-all-auth Settings
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/login'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
SOCIALACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/account/login"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/account/profile"
ACCOUNT_SIGNUP_FORM_CLASS = 'account.forms.SignupForm'


# South config
SOUTH_TESTS_MIGRATE = False
