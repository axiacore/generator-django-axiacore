#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

from <%= appNameLowerCase %>.views import <%= modelName %>Detail
from <%= appNameLowerCase %>.views import <%= modelName %>Create
from <%= appNameLowerCase %>.views import <%= modelName %>Update
from <%= appNameLowerCase %>.views import <%= modelName %>Delete

urlpatterns = patterns(
    '',

    # Detail.
    # Method: GET.
    url(
        r'^detail/(?P<pk>[-\d]+)/$',
        <%= modelName %>Detail.as_view(),
        name='detail',
    ),

    # Create.
    # Method: POST.
    url(
        r'^create/$',
        <%= modelName %>Create.as_view(),
        name='create',
    ),

    # Update.
    # Method: PUT/PATCH.
    url(
        r'^update/(?P<pk>[-\d]+)/$',
        <%= modelName %>Create.as_view(),
        name='update',
    ),

    # Delete.
    # Method: DELETE.
    url(
        r'^delete/(?P<pk>[-\d]+)/$',
        <%= modelName %>Create.as_view(),
        name='delete',
    ),

)
