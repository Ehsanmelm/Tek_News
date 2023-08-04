import pytest
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.test import APIClient, APITestCase 
from news.models import NewsModel 
import uuid
# from django.conf import settings

# settings.configure()

@pytest.mark.django_db
class TestNews(APITestCase ):
    client = APIClient()

    def setUp(self):
        self.news1 = NewsModel.objects.create(id=uuid.uuid4(),title='news1', description='Description1', resources='source1' , tags ='tag1')
        
    def test_list_news(self):
        response = self.client.get(f'/api/news/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_news_retrieve(self):
        news = NewsModel.objects.first()
        response = self.client.get(f'/api/news/{news.id}/')
        self.assertEqual(response.status_code ,status.HTTP_200_OK)

        
    def test_filter_backends(self):
        backend = DjangoFilterBackend()
        assert backend.filter_queryset(None, queryset=NewsModel.objects.all(), view=None) is not None

