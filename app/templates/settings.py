#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '{{ secret_key }}'
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEST_PROJECT_APPS = (
    'app',
)

INSTALLED_APPS = TEST_PROJECT_APPS + (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jenkins',

    'django_extensions',
    'compressor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_L10N = False
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

AXES_LOGIN_FAILURE_LIMIT = 10
AXES_USE_USER_AGENT = True
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = '403.html'

import sys
if 'test' in sys.argv:
    from app.test_settings import *  # pylint: disable=W0401,W0614
else:
    from app.local_settings import *  # pylint: disable=F0401,E0611
