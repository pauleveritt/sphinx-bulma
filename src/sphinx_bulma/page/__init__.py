"""

This is the generic "page" component that you get if a
document does not have a sb_type field.

"""


class PageComponent:
    sb_type = 'page'
    sb_layout = 'layout.html'

    def __init__(self, body):
        self.body = body

    @property
    def template_name(self):
        return 'page/page.html'
