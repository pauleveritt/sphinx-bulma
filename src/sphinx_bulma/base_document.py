class BaseDocument:
    document_type = 'article'
    layout = 'layout.html'

    def __init__(self, body):
        self.body = body

    @property
    def template_name(self):
        return '%s/%s.html' % (self.document_type, self.document_type)
