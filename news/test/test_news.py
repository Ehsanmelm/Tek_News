import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from news.models import NewsModel


@pytest.mark.django_db
class TestNews(APITestCase):
    client = APIClient()

    def setUp(self):
        self.news1 = NewsModel.objects.create(title='news1', description='Description1', resources='source1')

    def test_list_news(self):
        # url = reverse('news_list')
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_retrieve(self):
        response = self.client.get('/api/news/1/')
        self.assertEqual(response.status_code ,status.HTTP_200_OK)