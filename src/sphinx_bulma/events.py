"""

Callbacks that are registered as Sphinx events in __init__.setup

"""
from collections.abc import MutableMapping

# Document types
from .article import ArticleDocument
from .homepage import HomepageDocument
from .page import PageDocument

# Components
from .sidenav import SidenavComponent
from .logo import LogoComponent

document_types = dict(
    article=ArticleDocument,
    homepage=HomepageDocument,
    page=PageDocument
)
components = (
    SidenavComponent,
    LogoComponent
)


class Components(MutableMapping):
    def __init__(self, app):
        self.app = app
        self._storage = dict()

    def __getitem__(self, key):
        return self._storage[key]

    def add(self, component):
        # Make an instance of the component, with the app, and
        # store it with the key defined by the component.
        c = component(self.app)
        self._storage[c.name] = c

    def __setitem__(self, key, value):
        self._storage[key] = value

    def __delitem__(self, key):
        del self._storage[key]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)


def sb_startup(app, env, docnames):
    # Make the registry of components
    ac = app.components = Components(app)
    [ac.add(c) for c in components]


def sb_page_context(app, pagename, templatename, context, doctree):
    # If the page has a 'sb_type" field, use it to get the component
    # name. If not, default to the "page" component.
    document_type = context.get('meta', {}).get('sb_type', 'page')

    if document_type:
        # We have RST page with the magic marker at the top. Try to
        # get the page component that matches this magic marker.
        component = document_types.get(document_type)

        # Instantiate the component with what it needs
        body = context.get('body')
        document = component(body)

        # Put things into the Sphinx html evaluation context
        context['document'] = document
        context['sbc'] = app.components

        # Return the name of the template to use
        return document.template_name

    # Otherwise, return the template name. Unnecessary, as Sphinx will
    # do this anyway, but helps to make clear the contract.
    return templatename
