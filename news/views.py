from django.shortcuts import render , get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet , ViewSet
from rest_framework.views import APIView 
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import PageNumberPagination
from .models import  NewsModel
from .serializers import NewsSerializer
from .filters import NewsFilter
from .tasks import test_celery
from django.http import HttpResponse
# Create your views here.

class NewsViewSet(ModelViewSet):
    # test_celery.delay('i am sendig message')
    http_method_names = ['get']
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsFilter

    
def celery_test(request):
    test_celery.delay('i am in view')
    return HttpResponse('ok')