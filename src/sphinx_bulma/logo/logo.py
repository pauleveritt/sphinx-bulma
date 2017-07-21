class SBComponent:
    link_suffix = '.html'

    def get_target_uri(self, docname, typ=None):
        # type: (unicode, unicode) -> unicode
        return docname + self.link_suffix

    def pathto(otheruri, resource=False, baseuri=default_baseuri):
        default_baseuri = self.get_target_uri(pagename)
        if resource and '://' in otheruri:
            # allow non-local resources given by scheme
            return otheruri
        elif not resource:
            otheruri = self.get_target_uri(otheruri)
        uri = relative_uri(baseuri, otheruri) or '#'
        if uri == '#' and not self.allow_sharp_as_current_path:
            uri = baseuri
        return uri


class SBSite:
    """ All the static information from the site """
    config = {}


class LogoComponent(SBComponent):
    def __init__(self, site, body):
        pass

    @property
    def logo_url(self):
        return pathto('xxx', 1)

    @property
    def template(self):
        return 'path to template'

    def render(self):
        pass
