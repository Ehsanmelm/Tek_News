from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import NewsModel


@registry.register_document
class NewsDocuments(Document):
    id = fields.TextField()
    title = fields.TextField()
    description = fields.TextField(attr='description')
    tags = fields.TextField(
        attr='tags',
        fields={
            'raw': fields.KeywordField(),
        }
    )
    resources = fields.TextField(attr='resources')

    class Index:
        name = 'news'

    class Django:
        model = NewsModel
