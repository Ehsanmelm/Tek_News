from django.shortcuts import render, get_object_or_404
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from .models import NewsModel
from .serializers import NewsDocumentSerializer
from .tasks import NewsScraperTask
from .documents import NewsDocuments

# Create your views here.


class NewsDocumentView(DocumentViewSet):
    document = NewsDocuments
    serializer_class = NewsDocumentSerializer
    filter_backends = [
        SearchFilterBackend,
    ]
#  base on project document it will search between all necessary fields
    search_fields = ('tags', 'title', 'description')

#  in addition to run celery task every 30 second by refreshing page task will be execute too
    def list(self, request, *args, **kwargs):
        NewsScraperTask.delay('i am sending message')
        return super().list(request, *args, **kwargs)
