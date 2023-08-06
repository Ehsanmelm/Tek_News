from time import sleep
from celery import shared_task

@shared_task
def test_celery(message):
    print(" <<<<<<< send mail >>>>>>")
    print(message)
    sleep(5)
    print('<<<<<< after 5 second >>>>>')