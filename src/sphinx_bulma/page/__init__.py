"""

This is the generic "page" component that you get if a
document does not have a sb_type field.

"""
from sphinx_bulma.base_document import BaseDocument


class PageDocument(BaseDocument):
    document_type = 'page'