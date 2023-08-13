from django.db import models

# Create your models here.


class NewsModel(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title}"
    # class Meta:
    #     # managed = False
    #     db_table = 'newsmodel'
