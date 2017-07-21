class ArticleComponent:
    sb_type = 'article'
    sb_layout = 'layout2.html'

    def __init__(self, body):
        self.body = body

    @property
    def template_name(self):
        return 'article/article.html'
