#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """Renders the home page.
    """
    template_name = 'home.html'
