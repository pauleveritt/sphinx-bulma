import os

__version__ = "0.0.1"

__title__ = "sphinx_bulma"
__description__ = "Sphinx theme using Bulma CSS framework"
__uri__ = "https://github.com/pauleveritt/sphinx-bulma"
__doc__ = __description__ + " <" + __uri__ + ">"

__author__ = "Paul Everitt"
__email__ = "pauleveritt@me.org"

__license__ = "Apache License 2.0"
__copyright__ = "Copyright (c) 2017 Paul Everitt"


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context['sphinx_bulma_version'] = __version__


def setup(app):
    app.connect('html-page-context', update_context)
    return {'version': __version__,
            'parallel_read_safe': True}
