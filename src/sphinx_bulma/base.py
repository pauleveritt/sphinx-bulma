class BaseDocument:
    document_type = 'article'
    layout = 'layout.html'

    def __init__(self, body):
        self.body = body

    @property
    def template_name(self):
        return '%s/%s.html' % (self.document_type, self.document_type)


class BaseComponent:
    def __init__(self, app):
        self.app = app

    @property
    def template(self):
        return '%s/%s.html' % (self.name, self.name)

    def __call__(self, **kwargs):
        d = dict(component=self)
        context = {**kwargs, **d}
        return self.app.builder.templates.render(
            self.template,
            context
        )
