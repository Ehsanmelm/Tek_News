from django.shortcuts import render, get_object_or_404
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from .models import NewsModel
from .serializers import NewsDocumentSerializer
from .tasks import NewsScraperTask
from .documents import NewsDocuments

# Create your views here.


# class NewsViewSet(ModelViewSet):
#     http_method_names = ['get']
#     queryset = NewsModel.objects.all()
#     serializer_class = NewsSerializer
#     pagination_class = PageNumberPagination
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = NewsFilter

#     def list(self, request, *args, **kwargs):
#         NewsScraperTask.delay('i am sending message')
#         return super().list(request, *args, **kwargs)


class NewsDocumentView(DocumentViewSet):
    document = NewsDocuments
    serializer_class = NewsDocumentSerializer
    filter_backends = [
        SearchFilterBackend,
    ]
    search_fields = ('tags', )
    search_fields = ('tags', 'tags__icontains', )

    def list(self, request, *args, **kwargs):
        NewsScraperTask.delay('i am sending message')
        return super().list(request, *args, **kwargs)
