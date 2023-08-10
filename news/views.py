import django_filters
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, FilteringFilterBackend
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import PageNumberPagination
from .models import NewsModel
from .serializers import NewsSerializer, NewsDocumentSerializer
from .filters import NewsFilter
from .tasks import NewsScraperTask
from .documents import NewsDocuments

# Create your views here.


class NewsViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsFilter

    def list(self, request, *args, **kwargs):
        NewsScraperTask.delay('i am sending message')
        return super().list(request, *args, **kwargs)


class NewsDocumentView(DocumentViewSet):
    document = NewsDocuments
    serializer_class = NewsDocumentSerializer
    filter_backends = [
        SearchFilterBackend,
    ]
    search_fields = ('tags', 'tags__icontains', )

    def list(self, request, *args, **kwargs):
        NewsScraperTask.delay('i am sending message')
        return super().list(request, *args, **kwargs)

# class NewsDocumentFilter(django_filters.FilterSet):
#     tags = django_filters.CharFilter(method='filter_tags')

#     def filter_tags(self, queryset, name, value):
#         tags = value.split(',')  # Assuming the tags are comma-separated
#         return queryset.filter(tags__in=tags)

#     class Meta:
#         model = NewsDocuments
#         fields = ['tags']


# class NewsDocumentView(DocumentViewSet):
#     document = NewsDocuments
#     serializer_class = NewsDocumentSerializer

#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filterset_class = NewsDocumentFilter
