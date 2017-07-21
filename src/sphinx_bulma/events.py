"""

Callbacks that are registered as Sphinx events in __init__.setup

"""
from collections.abc import MutableMapping

from .article import ArticleDocument
from .homepage import HomepageComponent
from .page import PageComponent
from .sidenav import SidenavComponent

document_types = dict(
    article=ArticleDocument,
    homepage=HomepageComponent,
    page=PageComponent
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
        self._storage[c.sb_type] = c

    def __setitem__(self, key, value):
        self._storage[key] = value

    def __delitem__(self, key):
        del self._storage[key]

    def __iter__(self):
        return iter(self._storage)

    def __len__(self):
        return len(self._storage)


# class Site:
#     def __init__(self, app):
#         self.app = app
#         self.components = [
#             ArticleDocument,
#             HomepageComponent,
#             PageComponent
#         ]
#
#     def get_component(self, component_name):
#         # Find the first component with a sb_name that matches
#         # the asked-for name, or None
#         return next(
#             (x for x in self.components
#              if hasattr(x, 'sb_type') and x.document_type == component_name),
#             None)
#
#
def sb_startup(app, env, docnames):
    # Make a "site"
    if not hasattr(app, 'site'):
        # TODO this might be a bad idea, might get pickled
        # app.site = Site(app)
        ac = app.components = Components(app)
        ac.add(SidenavComponent)
    else:
        raise NotImplementedError


def sb_page_context(app, pagename, templatename, context, doctree):
    # If the page has a 'sb_type" field, use it to get the component
    # name. If not, default to the "page" component.
    document_type = context.get('meta', {}).get('document_type', 'page')

    if document_type:
        # We have RST page with the magic marker at the top. Try to
        # get the page component that matches this magic marker.
        component = document_types.get(document_type)  # site.get_component(document_type)

        # Instantiate the component with what it needs
        body = context.get('body')
        resource = component(body)

        # Put things into the Sphinx html evaluation context
        context['resource'] = resource
        context['sbc'] = app.components

        # Return the name of the template to use
        return resource.template_name

    # Otherwise, return the template name. Unnecessary, as Sphinx will
    # do this anyway, but helps to make clear the contract.
    return templatename
