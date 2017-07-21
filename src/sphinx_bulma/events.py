"""

Callbacks that are registered as Sphinx events in __init__.setup

"""

from .article import ArticleComponent


class Site:
    def __init__(self):
        self.components = [ArticleComponent]

    def get_component(self, component_name):
        return next(
            (x for x in self.components
             if x.sb_type == component_name),
            None)


def sb_startup(app, env, docnames):
    # Make a "site"
    if not hasattr(env, 'site'):
        env.site = Site()


def sb_page_context(app, pagename, templatename, context, doctree):

    # Find out which kind of page component this is, if meta even exists
    sb_type = context.get('meta', {}).get('sb_type')

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
