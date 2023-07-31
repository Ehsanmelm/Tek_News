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

# Create your views here.

class NewsViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsFilter

    