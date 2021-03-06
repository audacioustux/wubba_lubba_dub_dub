"""
Django settings for nobinalo project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from pathlib import Path
import json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

with open('secrets.json') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exceptions'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = '{0} variable not found'.format(setting)
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'graphql_jwt.middleware.JSONWebTokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'nobinalo.urls'

WSGI_APPLICATION = 'nobinalo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nobinalo',
        'USER': 'audacioustux',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

# Graphene API
GRAPHENE = {
    'SCHEMA': 'nobinalo.schema.schema',
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tangimhossain1@gmail.com'
EMAIL_HOST_PASSWORD = get_secret('SMTP_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# user config

AUTH_USER_MODEL = 'user.User'

Bad_Word = [
    "anal",
    "anus",
    "arse",
    "ass",
    "asshole",
    "ballsack",
    "balls",
    "bastard",
    "bitch",
    "biatch",
    "bloody",
    "blowjob",
    "bollock",
    "bollok",
    "boner",
    "boob",
    "bugger",
    "bum",
    "butt",
    "buttplug",
    "clitoris",
    "cock",
    "coon",
    "crap",
    "cunt",
    "damn",
    "dick",
    "dildo",
    "dyke",
    "fag",
    "feck",
    "fellate",
    "fellatio",
    "felching",
    "fuck",
    "fudgepacker",
    "flange",
    "Goddamn",
    "hell",
    "homo",
    "jerk",
    "jizz",
    "knobend",
    "labia",
    "lmao",
    "lmfao",
    "muff",
    "nigger",
    "nigga",
    "omg",
    "penis",
    "piss",
    "poop",
    "prick",
    "pube",
    "pussy",
    "porn",
    "queer",
    "scrotum",
    "sex",
    "shit",
    "sh1t",
    "slut",
    "smegma",
    "spunk",
    "tit",
    "tosser",
    "turd",
    "twat",
    "vagina",
    "wank",
    "whore",
    "wtf",
    "xxx"
]
