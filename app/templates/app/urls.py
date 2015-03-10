#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomeView

# Django admin.
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns = patterns('',

    # Home.
    url(
        r'^$',
        HomeView.as_view(),
        name='home',
    ),
)
