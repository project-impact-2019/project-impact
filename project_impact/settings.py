"""
Django settings for project_impact project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dontenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dontenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8to63ay#nc1$#2cv808x_^!ybzn4pdlztvtmxo%_5+_ius)u=$'

# SECURITY WARNING: don't run with debug turned on in production!
in_production = bool(os.getenv('PRODUCTION'))
DEBUG = not in_production

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Third-party apps
    'registration',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Personal apps 
    'core', 


    # Third-party apps
    'debug_toolbar',
    'django_filters',
    'phonenumber_field',

]

# Custom User Authentication
AUTH_USER_MODEL = 'core.User'

MIDDLEWARE = [
    # Third-party apps
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_impact.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_impact.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Django-debug-toolbar settings

INTERNAL_IPS = ['127.0.0.1']

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__),'static'),)

STATIC_URL = '/static/'



# Registration

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False
LOGIN_REDIRECT_URL = '/'

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())


# Email Settings for Registration
EMAIL_HOST = 'smtp.gmail.com'  # since you are using a gmail account
EMAIL_PORT = 587  # Gmail SMTP port for TLS
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)

PHONENUMBER_DEFAULT_REGION = 'US'



# Twilio Chat Settings
TWILIO_ACCT_SID = os.environ['TWILIO_ACCT_SID']
TWILIO_CHAT_SID = os.environ['TWILIO_CHAT_SID']
TWILIO_SYNC_SID = os.environ['TWILIO_SYNC_SID']
TWILIO_API_SID = os.environ['TWILIO_API_SID']
TWILIO_API_SECRET = os.environ['TWILIO_API_SECRET']




