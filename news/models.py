from django.db import models

# Create your models here.


class NewsModel(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)

    # class Meta:
    #     # managed = False
    #     db_table = 'newsmodel'
