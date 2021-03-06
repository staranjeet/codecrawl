"""
Django settings for codecrawl project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%6p6^qp1(1pxb%i67e$wn+*=xkl##byoc%m_tpn2ewv1mfmp25'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
     ('Deshraj', 'deshrajdry@gmail.com'),
     ('Taranjeet','reachtotj@gmail.com'),
)

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'codecal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'codecrawl.urls'

WSGI_APPLICATION = 'codecrawl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'codecrawldb',
        'USER':'tj',
        'PASSWORD':'gameover',
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
            os.path.join( PROJECT_ROOT, 'static'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
TEMPLATE_DIRS = [(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'codecaltemplates'))]

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
