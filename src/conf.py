# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = ''
copyright = '2022, This guideline is licenced under the "Creative Commons Attribution 4.0 International (CC BY 4.0)" licence'
author = 'TUM Chair of Geoinformatics'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinxemoji.sphinxemoji',
    'sphinx.ext.autosectionlabel',
    'sphinx_toolbox.collapse',
    'sphinx_fontawesome',
    #'sphinx_rtd_dark_mode'
]



#default_dark_mode = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'




html_last_updated_fmt = '%b %d, %Y'
html_favicon = ''
html5_writer = True
html_logo = 'road2citygml3_logo1.png'
html_show_sourcelink = False
html_theme_options = {
 
    'style_external_links': True,
    'logo_only': True,
    'display_version': False
 
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Enable numref
numfig = True
numfig_secnum_depth = 0
numfig_format={'code-block': 'XML example %s', 'figure': 'Figure %s', 'section': 'Section %s', 'table': 'Table %s'  }

html_show_sphinx = False


