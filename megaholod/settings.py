import os
HOST = os.environ['HOST']
if not HOST == 'local':
    BASE_DIR = os.environ['DJ_PROJECT_HOME']
else:
    BASE_DIR = os.getcwd()
# Added to help use env variables
def env_var(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

DEBUG = env_var('DJ_DEBUG', False) #Unless env var is set to True, debug is off
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Kirill Shershen', 'shkipc@gmail.com'),
)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_PASSWORD = 'GtO4ymYNPLuILgGt3yKA'
EMAIL_HOST_USER = 'django_mail@mail.ru'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = 'django_mail@mail.ru'
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

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
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'feedback.context_processors.feedback_form',
    'news.context_processors.get_lastnews',
    'product.context_processors.get_objects',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)
# Additional locations of static files
STATICFILES_DIRS = (
    'g:\work\py\megaholod\static',
    'd:\work\django\megaholod\static',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['DJ_SECRET_KEY']

# List of callables that know how to import templates from various sources.
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

ROOT_URLCONF = 'megaholod.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'megaholod.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'), 
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'filebrowser',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'news',
    'product',
    'south',
    'feedback',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT 
FILEBROWSER_MEDIA_URL = MEDIA_URL 
FILEBROWSER_STATIC_ROOT = STATIC_ROOT 
FILEBROWSER_STATIC_URL = STATIC_URL 
URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/' 
PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/' 
# URL_TINYMCE = STATIC_URL + 'tiny_mce/' 
# PATH_TINYMCE = STATIC_ROOT + 'tiny_mce/' 

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

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
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                     '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file':{
            'level' : 'INFO',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : os.path.join(BASE_DIR, 'logs/main.log'),
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_false'],
        },
        'debug_file':{
            'level' : 'DEBUG',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : os.path.join(BASE_DIR, 'logs/main_debug.log'),
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_true'],
        },
        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        '': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "DEBUG",
        },
    }
}

if HOST != 'locum':
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    DATABASES['default']['NAME'] = 'megaholod'
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'kxekxe_megahol39',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'kxekxe_megahol39',
            'PASSWORD': 'hWy78lQZ',
            'HOST': 'mysql2.locum.ru',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }
    MEDIA_ROOT = '/home/hosting_kxekxe/projects/megaholod/media'
    STATIC_URL = '/static/'
    STATIC_ROOT = '/home/hosting_kxekxe/projects/megaholod/static'
    ADMIN_MEDIA_PREFIX = '/static/admin/'