"""

Handle the homepage.

"""


class HomepageComponent:
    sb_type = 'homepage'
    sb_layout = 'layout.html'

    def __init__(self, body):
        self.body = body

    @property
    def template_name(self):
        return 'homepage/homepage.html'
