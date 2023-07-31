from rest_framework import serializers
from .models import NewsModel 



class NewsSerializer(serializers.ModelSerializer):
    # tags= TagSerializer(many=True)
    class Meta:
        fields = ['id' , 'title' , 'description' , 'resources' , 'tags']
        model = NewsModel
