from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path


elastic_router = SimpleRouter(trailing_slash=False)
elastic_router.register(
    r'news/', views.NewsDocumentView, basename='elastic_news')


urlpatterns = elastic_router.urls
