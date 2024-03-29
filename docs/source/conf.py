# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os 
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Packaging Journal'
copyright = '2022, Yuqiu (Ian) Yang'
author = 'Yuqiu (Ian) Yang'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # A theme
    'sphinx_rtd_theme',
    # For automatic doc generation
    'sphinx.ext.autodoc',
    # Just some info
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    # For Google and Numpy docstring
    'sphinx.ext.napoleon',]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = "../../assets/logo.png"
html_static_path = ['_static']
