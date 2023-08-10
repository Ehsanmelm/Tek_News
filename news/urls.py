from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path

router = DefaultRouter()
router.register('news', views.NewsViewSet, basename='news_list')

elastic_router = SimpleRouter(trailing_slash=False)
elastic_router.register(
    r'elastic_news', views.NewsDocumentView, basename='elastic_news')


urlpatterns = router.urls + elastic_router.urls
