# -*- coding: utf-8 -*-

# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']

source_suffix = '.rst'

source_encoding = 'utf-8'

master_doc = 'index'

project = u'{{ project_name }}'
copyright = u'2013, AxiaCore'

version = '1.0'
release = '1.0'

language = 'es'

exclude_trees = []

pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

html_theme = 'nature'

html_theme_path = ['_themes']

html_logo = '_static/images/axiacore-logo-small.png'

html_static_path = ['_static']


# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
    ('index', 'SphinxDoc.tex', u'Documentación {{ project_name }}', u'AxiaCore', 'manual'),
]
