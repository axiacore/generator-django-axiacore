#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns

from <%= appNameLowerCase %>.views import <%= appName %>Detail
from <%= appNameLowerCase %>.views import <%= appName %>Create
from <%= appNameLowerCase %>.views import <%= appName %>Update
from <%= appNameLowerCase %>.views import <%= appName %>Delete

urlpatterns += patterns(
    '',

    # Detail.
    # Method: GET.
    url(
        r'^<%= appNameLowerCase %>s-detail/(?P<pk>[-\d]+)/$',
        <%= appName %>Detail.as_view(),
        name='detail',
    ),

    # Create.
    # Method: POST.
    url(
        r'^<%= appNameLowerCase %>s-create/$',
        <%= appName %>Create.as_view(),
        name='create',
    ),

    # Update.
    # Method: PUT/PATCH.
    url(
        r'^<%= appNameLowerCase %>s-update/(?P<pk>[-\d]+)/$',
        <%= appName %>Create.as_view(),
        name='update',
    ),

    # Delete.
    # Method: DELETE.
    url(
        r'^<%= appNameLowerCase %>s-delete/(?P<pk>[-\d]+)/$',
        <%= appName %>Create.as_view(),
        name='delete',
    ),

)
