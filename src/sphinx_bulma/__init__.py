import os

from sphinx_bulma import events

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


def get_html_templates_path():
    """Return path to theme's template folder.

    Used by the doc project's config.py to hook into the template
    setup.
    """

    pkgdir = os.path.abspath(os.path.dirname(__file__))

    # We're going to store templates in components, not a template dir
    return [os.path.join(pkgdir)]


def setup(app):
    app.connect('env-before-read-docs', events.sb_startup)
    app.connect('html-page-context', events.sb_page_context)
    return {'version': __version__,
            'parallel_read_safe': True}
