class SidenavComponent:
    name = 'sidenav'
    _template = 'sidenav/sidenav.html'

    def __init__(self, app):
        self.app = app

    def __call__(self, **kwargs):
        d = dict(component=self)
        context = {**kwargs, **d}
        return self.app.builder.templates.render(
            self._template,
            context
        )
