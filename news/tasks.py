from scrapy import cmdline
from celery import shared_task


@shared_task
def NewsScraperTask(message):
    cmdline.execute("scrapy runspider zoomit_scrap/recent_news.py".split())
