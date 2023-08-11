from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import NewsModel
from .documents import NewsDocuments


# class NewsSerializer(serializers.ModelSerializer):
#     # tags= TagSerializer(many=True)
#     class Meta:
#         fields = ['id', 'title', 'description', 'resources', 'tags']
#         model = NewsModel


class NewsDocumentSerializer(DocumentSerializer):
    class Meta:
        document = NewsDocuments
        fields = ('id', 'title', 'description', 'resources', 'tags')
