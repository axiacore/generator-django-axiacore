#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
BWR = 'bower_components/{0}'

PIPELINE_CSS = {
    'global_css': {
        'source_filenames': (),
        'output_filename': 'css/styles.min.css',
    },
}

PIPELINE_JS = {
    'global_js': {
        'source_filenames': (),
        'output_filename': 'js/global.min.js',
    },
}
