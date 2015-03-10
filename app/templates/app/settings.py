#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '{{ secret_key }}'
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# django-grappelli
GRAPPELLI_ADMIN_TITLE = u'<%= adminSiteName %>'
GRAPPELLI_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

AXES_LOGIN_FAILURE_LIMIT = 10
AXES_USE_USER_AGENT = True
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = '403.html'

# Have pipeline settings in a separate file.
settings_file = __import__('app.pipeline_settings').pipeline_settings
for setting_value in dir(settings_file):
    locals()[setting_value] = getattr(settings_file, setting_value)

import sys
if 'test' in sys.argv:
    from app.test_settings import *  # pylint: disable=W0401,W0614
else:
    from app.local_settings import *  # pylint: disable=F0401,E0611
