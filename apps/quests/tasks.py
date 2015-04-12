# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

__author__ = 'Last G'

from celery import shared_task


@shared_task
def check_answer(answer):
    answer.check_answer()