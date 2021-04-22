"""
Django settings for mysiteWeb project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from pymongo import MongoClient #va avec la bd


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i9!x0h1rk1#t!i-6cn-*1ojj8e8t^bmq^_7t%g1fqy%+tb@19q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','3b1447335c5a','7876d1417f49.ngrok.io']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'crispy_forms',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.erp',
    'apps.user',
   # 'django_telegrambot',
    'django_tgbot',
    'django_telegram_login',
]

HOOK_EVENTS = {
    # 'any.event.name': 'App.Model.Action' (created/updated/deleted)
    'utilisateur.added': 'apps.users.models.Utilisateur.created',
    'user.logged_in': None
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

MONGO_CLIENT = MongoClient("mongodb://localhost:27017/") #on peut l'enlever

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'configue',
        # 'USER': 'root',
        # 'PASSWORD': '',
        # 'PORT': '3306'
    }
}

TELEGRAM_BOT_NAME = 'test1steve_bot'
TELEGRAM_BOT_TOKEN='1793178760:AAFxxH4YJ-cP7Ybu7oI-ZOs-aVOOg9rQbYo'
BOT_URL='https://api.telegram.org/bot%s/'%TELEGRAM_BOT_TOKEN
BOT_CHAT_ID='1745381202'
TELEGRAM_LOGIN_REDIRECT_URL = 'https://7876d1417f49.ngrok.io/test'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
