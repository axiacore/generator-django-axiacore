#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<%= dbName %>',
        'USER': '<%= dbUser %>',
        'PASSWORD': '<%= dbPass %>',
    }
}

EMAIL_HOST = '--DEFINE--'
EMAIL_HOST_USER = '--DEFINE--'
EMAIL_HOST_PASSWORD = '--DEFINE--'

INTERCOM_APP_ID = '--DEFINE--'
GOOGLE_ANALYTICS_CODE = '--DEFINE--'

SECRET_KEY = '--DEFINE--'

# Uncomment for development
# DEBUG = True
# TEMPLATE_DEBUG = True
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     },
#     'sessions': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/tmp/django_cache',
#     }
# }
