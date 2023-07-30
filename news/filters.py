from django_filters.rest_framework import FilterSet
from .models import NewsModel


class NewsFilter(FilterSet):
    class Meta:
        model = NewsModel
        fields = {
            # 'tags': ['exact'],
            'tags': ['icontains'],
        }
