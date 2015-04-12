# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.task_board),
                       url(r'^score/', views.score_board),
                       url(r'^answer/$', views.answer_board),
                       url(r'^answer/latest/$', views.get_last_answers),
                       url(r'^answer/more/$', views.get_more_answers),
)
