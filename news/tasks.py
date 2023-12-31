from scrapy import cmdline
from celery import shared_task
import subprocess
from django_elasticsearch_dsl import Index
from .models import NewsModel
from elasticsearch_dsl.connections import connections


@shared_task
def NewsScraperTask(message):
    # I had handled it by two way(signals and this way ) but because of doing celery task repeatedly i prefered it should be more accurate 
    subprocess.call(["python", "manage.py", "search_index", "--rebuild", "-f"])
    cmdline.execute("scrapy runspider zoomit_scrap/recent_news.py".split())
