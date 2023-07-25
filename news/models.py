from django.db import models

# Create your models here.

class TagModel(models.Model):
    tag_name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"{self.tag_name}"

