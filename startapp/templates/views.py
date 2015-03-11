#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Resource name: Post
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import CreateView


class <%= modelName %>Detail(DetailView):
    """ Shows <%= modelName %> detail.
    """
    model = <%= modelName %>
    template_name = '<%= modelNameLowerCase %>_detail.html'


class <%= modelName %>Create(CreateView)
    """ Handle the creation of a new <%= modelName %>.
    """
    model = <%= modelName %>


class <%= modelName %>Update(UpdateView)
    """ Updates an existing <%= modelName %>.
    """
    model = <%= modelName %>


class <%= modelName %>Delete(DeleteView)
    """ Deletes a <%= modelName %>.
    """
    model = <%= modelName %>
