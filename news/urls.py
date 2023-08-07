from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('news', views.NewsViewSet, basename='news_list')

urlpatterns = router.urls

# urlpatterns += [
#     path('test', views.celery_test)
# ]
