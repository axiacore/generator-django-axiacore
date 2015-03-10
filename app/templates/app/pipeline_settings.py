#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
BWR = 'bower_components/{0}'

PIPELINE_CSS = {
    'global_css': {
        'source_filenames': (<% if (cssFramework == 'materialize' ) { %>
            BWR.format('materialize/dist/css/materialize.min.css'),
        <% } %>
            'css/styles.css',
        ),
        'output_filename': 'css/styles.min.css',
    },
}

PIPELINE_JS = {
    'global_js': {
        'source_filenames': (
            BWR.format('jquery/dist/jquery.min.js'),<% if (cssFramework == 'materialize' ) { %>
            BWR.format('materialize/dist/js/materialize.min.js'),
         <% } %>
        ),
        'output_filename': 'js/global.min.js',
    },
}
