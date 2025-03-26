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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

def setup(app):
   app.add_css_file('css/custom.css')


# -- Project information -----------------------------------------------------

project = 'UNICORE Docs'
author = '2025 UNICORE'
copyright = author
version = 'stable'
language = 'en'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinxemoji.sphinxemoji',
    'sphinx.ext.autosectionlabel',
    'm2r2'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*.bak", "*.txt", "*.rest"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'                # read the docs (external)
html_theme_options = {
    "navigation_with_keys": True,
}
html_theme_path = ["_themes", ]
html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    #'logo_only': False,
    #'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    #'vcs_pageview_mode': 'blob',
    #'style_nav_header_background': '#2980B9',
    'style_nav_header_background': '#0080C0',
    # Toc options
    'collapse_navigation': False,
    #'sticky_navigation': True,
    #'navigation_depth': 4,
    #'includehidden': True,
    #'titles_only': False
}
html_logo = "_static/logo-unicore.png"
html_title = "UNICORE Docs"

#html_sidebars = {
#   '**': ['globaltoc.html'],
#}

numfig = True
html_show_sourcelink = False
html_show_sphinx = False


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

"""
 Tells the project to use sphinx pygments for color coding code examples.
"""

pygments_style = 'sphinx'
   
html_context = {
  "display_github": False, # Add 'Edit on Github' link instead of 'View page source'
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# link uftp-docs project with intersphinx
intersphinx_mapping = {
    "uftp-docs": ("https://uftp-docs.readthedocs.io/en/latest/", None),
}

# We recommend adding the following config value.
# Sphinx defaults to automatically resolve *unresolved* labels using all your Intersphinx mappings.
# This behavior has unintended side-effects, namely that documentations local references can
# suddenly resolve to an external location.
# See also:
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]

# Make sure the target is unique
#
# it could raise some warnings to duplicated labels used in several files or in the same file,
# but you could supress such warnings (see the option below)
autosectionlabel_prefix_document = True

# supress warning for dublicate labels (e.g. section titles "Input", "Output", etc)
suppress_warnings = ['autosectionlabel.*']