#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
import os
import json

from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    def get_project_version(self):
        """Return the project version
        """
        CACHE_KEY = 'admin_project_version'
        version = cache.get(CACHE_KEY)
        if not version:
            file_path = os.path.join(settings.BASE_DIR, 'package.json')
            with open(file_path, 'r') as v_file:
                data = json.load(v_file)
                version = data['version']
                cache.set(CACHE_KEY, version)

        return version

    def init_with_context(self, context):
        admin_models = (
            'django.contrib.sites.*',
            'django.contrib.auth.*',
        )

        if context['user'].is_superuser:
            self.children.append(modules.AppList(
                u'Administración de Servidor',
                column=1,
                css_classes=('grp-closed',),
                models=admin_models,
            ))

            self.children.append(modules.LinkList(
                u'Tareas de Administración',
                column=2,
                children=([
                    {
                        'title': 'Regenerar cache',
                        'url': reverse('clean_cache'),
                        'external': False,
                    },
                ])
            ))

        self.children.append(modules.ModelList(
            u'Administración de contenidos',
            column=1,
            models=(
                'app.*',
            ),
        ))

        self.children.append(modules.RecentActions(
            u'Acciones Recientes',
            column=3,
            limit=5,
            collapsible=False,
        ))

        self.children.append(modules.LinkList(
            u'Soporte',
            collapsible=False,
            column=3,
            children=(
                ['Abrir un ticket de soporte', '#support'],
            ),
            post_content="""
<ul class="grp-listing-small">
    <li class="grp-row">
        <p>Las solicitudes se pueden enviar a
        <strong>soporte@axiacore.com</strong></p>
        <p>El horario de atención es de 8:00AM a 12:00M y
        de 2:00PM a 5:00PM en días hábiles.</p>
        <p>Versión: <strong>{0}</strong></p>
    </li>
</ul>""".format(self.get_project_version())))
