from rest_framework import serializers
from .models import NewsModel , TagModel

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id' , 'title' , 'description' , 'resources' , 'tag']
        model = NewsModel
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id' , 'tag_name']
        model = TagModel