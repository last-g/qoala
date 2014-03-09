"""
Django settings for qoala project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DATA_DIR = os.path.join(BASE_DIR, 'data')
TASKS_DIR = os.path.join(DATA_DIR, 'tasks')
TASKS_DATA_DIR = os.path.join(DATA_DIR, 'tmptasks')

# App/Library Paths
sys.path.append(os.path.join(BASE_DIR, 'apps'))
sys.path.append(os.path.join(BASE_DIR, 'lib'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3tqlw0=fqml%ivszvim&8)$(%&#_69cmulxm-4ai-fib9=+#%*'

# Salt for generating tasks patterns

TASK_SALT = "asdkajdlkasjdlkajsdlkajlskdjalksdjkl"

ANSWERS_PER_MINUTE = 30

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = False

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "teams.Team"
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'teams.auth.TokenAuthBackend')

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/teams/login'
LOGOUT_URL = '/teams/logout'


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    # Third-party apps, patches, fixes
    'djcelery',

    # Database migrations
    'south',

    # Global context
    'base',

    # Own apps
    'teams',
    'quests',
    'board'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'qoala.urls'

WSGI_APPLICATION = 'qoala.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

TIME_ZONE = 'Asia/Yekaterinburg'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_URL = '/static/'

# Sessions
#
# By default, be at least somewhat secure with our session cookies.
SESSION_COOKIE_HTTPONLY = True


def custom_show_toolbar(request):
    """ Only show the debug toolbar to users with the superuser flag. """
    return request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': 'qoala.settings.custom_show_toolbar',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
}

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
#BROKER_URL = 'amqp://guest:guest@localhost//'


