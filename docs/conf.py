# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Slackfin'
copyright = '2023, California Institute of Technology'   # pylint: disable=redefined-builtin
author = 'Glenn Bach, Chris Malek'

# The full version, including alpha/beta/rc tags
release = '0.2.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinxcontrib.images',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

add_function_parentheses: bool = False
add_module_names: bool = False

autodoc_member_order = 'groupwise'

# Make Sphinx not expand all our Type Aliases
autodoc_type_aliases = {}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_context = {
    "display_github": True,  # Integrate github
    "github_user": "caltech-imss-ads",  # Username
    "github_repo": "slackfin",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/docs/",  # Path in the checkout to the docs root
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': True,
    'navigation_depth': 3,
    "show_prev_next": False,
    # "logo": {
    #     "image_light": "wildewidgets_logo.png",
    #     "image_dark": "wildewidgets_dark_mode_logo.png",
    #     "text": "Django-Wildewidgets",
    # },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/caltechads/slackfin",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
    ],
}
