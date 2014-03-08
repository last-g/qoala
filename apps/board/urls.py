from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.task_board),
                       url(r'^score/', views.score_board),
                       url(r'^answer/$', views.answer_board),
                       url(r'^answer/latest/$', views.get_last_answers)
                       #                       url(r'open/(?P<task_id>\d+)', views.open_task),
                       #                       url(r'answer/(?P<task_id>\d+)', views.answer_task),
                       #                       url(r'check/(?P<answer_id>\d+)', views.check_answer)
)
