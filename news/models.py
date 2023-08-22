from django.db import models

# Create your models here.


class NewsModel(models.Model):
    # id will save in uuid form in scrap part
    id = models.CharField(primary_key=True, max_length=36)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)
    # all field have blank and null equal true because of that I had thought it may be a news that doesnt have a part in zoomit site

    def __str__(self) -> str:
        return f"{self.title}"
    # class Meta:
    #     # managed = False
    #     db_table = 'newsmodel'

#  i remove tag part because there wasnt any important action on them 