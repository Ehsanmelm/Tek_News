from rest_framework import serializers
from .models import NewsModel , TagModel


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['id' ,'tag_name']
#         model = TagModel


class NewsSerializer(serializers.ModelSerializer):
    # tags= TagSerializer(many=True)
    class Meta:
        fields = ['id' , 'title' , 'description' , 'resources' , 'tags']
        model = NewsModel
