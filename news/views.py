from django.shortcuts import render , get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import TagModel , NewsModel
from .serializers import NewsSerializer
from .filters import NewsFilter

# Create your views here.

class NewsViewSet(ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsFilter

    