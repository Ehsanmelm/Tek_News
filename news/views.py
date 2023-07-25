from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import TagModel , NewsModel
from .serializers import NewsSerializer
# Create your views here.

class NewsViewSet(ViewSet.ReadOnlyModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    
    