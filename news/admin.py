from django.contrib import admin
from .models import NewsModel , TagModel

# Register your models here.

admin.site.register(NewsModel)
admin.site.register(TagModel)