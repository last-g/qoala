__author__ = 'Last G'

from celery import shared_task


@shared_task
def check_answer(answer):
    answer.check()