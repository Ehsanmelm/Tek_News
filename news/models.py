from django.db import models

# Create your models here.

class TagModel(models.Model):
    tag_name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.tag_name}"

class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    resources = models.TextField()
    tags = models.ManyToManyField(TagModel)

    def __str__(self) -> str:
        return f"{self.title}"