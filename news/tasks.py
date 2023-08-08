import scrapy
from scrapy import cmdline
from time import sleep
from celery import shared_task
from zoomit_scrap.recent_news import MainSpider


@shared_task
def NewsScraperTask(message):
    cmdline.execute("scrapy runspider zoomit_scrap/recent_news.py".split())
