import pytest
from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.test import APIClient, APITestCase 
from news.models import NewsModel ,TagModel
# from django.conf import settings

# settings.configure()

@pytest.mark.django_db
class TestNews(APITestCase ):
    client = APIClient()

    # def setUp(self):
    #     self.news1 = NewsModel.objects.create(title='news1', description='Description1', resources='source1')

    def setUp(self):
        tag1 = TagModel.objects.create(tag_name='Tag 1')
        tag2 = TagModel.objects.create(tag_name='Tag 2')
        self.news1 = NewsModel.objects.create(title='news1', description='Description1', resources='source1')
        self.news1.tags.add(tag1, tag2)
        
    def test_list_news(self):

        # url = reverse('news_list')
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_retrieve(self):
        response = self.client.get('/api/news/1/')
        self.assertEqual(response.status_code ,status.HTTP_200_OK)


    def test_filter_backends(self):
        backend = DjangoFilterBackend()
        assert backend.filter_queryset(None, queryset=NewsModel.objects.all(), view=None) is not None

