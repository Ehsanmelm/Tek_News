from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', views.NewsViewSet , basename=  'news_list')

urlpatterns = router.urls