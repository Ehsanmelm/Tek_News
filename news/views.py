from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import PageNumberPagination
from .models import NewsModel
from .serializers import NewsSerializer
from .filters import NewsFilter
from .tasks import NewsScraperTask
from django.http import HttpResponse
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

# def celery_test(request):
#     NewsScraperTask.delay('i am in view')
#     return HttpResponse('ok')
