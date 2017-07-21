"""

Callbacks that are registered as Sphinx events in __init__.setup

"""

from .article import ArticleComponent
from .homepage import HomepageComponent
from .page import PageComponent
from .logo import LogoComponent


class Site:
    def __init__(self):
        self.components = [
            ArticleComponent,
            HomepageComponent,
            LogoComponent,
            PageComponent
        ]

    def get_component(self, component_name):
        # Find the first component with a sb_name that matches
        # the asked-for name, or None
        return next(
            (x for x in self.components
             if hasattr(x, 'sb_type') and x.sb_type == component_name),
            None)


def sb_startup(app, env, docnames):
    # Make a "site"
    if not hasattr(env, 'site'):
        env.site = Site()


def sb_page_context(app, pagename, templatename, context, doctree):
    # If the page has a 'sb_type" field, use it to get the component
    # name. If not, default to the "page" component.
    sb_type = context.get('meta', {}).get('sb_type', 'page')

    if sb_type:
        # We have RST page with the magic marker at the top. Try to
        # get the page component that matches this magic marker.
        site = app.env.site
        component = site.get_component(sb_type)

        # Instantiate the component with what it needs
        body = context.get('body')
        resource = component(body)

        # Put things into the Sphinx html evaluation context
        context['site'] = site
        context['resource'] = resource

        # Return the name of the template to use
        return resource.template_name

    # Otherwise, return the template name. Unnecessary, as Sphinx will
    # do this anyway, but helps to make clear the contract.
    return templatename
