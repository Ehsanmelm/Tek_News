from scrapy import cmdline
from celery import shared_task
import subprocess
from django_elasticsearch_dsl import Index
from .models import NewsModel
from elasticsearch_dsl.connections import connections


# @shared_task
# def update_elastic_index():

#     # Connect to Elasticsearch
#     connections.create_connection(hosts=['elasticsearch'])

#     # Define the Elasticsearch index
#     index = Index('news')

#     # Add mapping for your model
#     index.document(NewsModel)

#     # Fetch data from the database
#     data = NewsModel.objects.all()  # Replace with your query

#     # Delete previous documents
#     index.delete()

#     # Index new documents
#     for obj in data:
#         obj.save()
#         index.save(obj)

#     # Refresh the index
#     index.refresh()


@shared_task
def NewsScraperTask(message):
    subprocess.call(["python", "manage.py", "search_index", "--rebuild", "-f"])
    cmdline.execute("scrapy runspider zoomit_scrap/recent_news.py".split())
    # update_elastic_index.delay()
