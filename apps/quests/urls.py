from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^open/(?P<task_id>\d+)/$', views.open_task),
                       url(r'^answer/(?P<task_id>\d+)/$', views.answer_task),
                       url(r'^check/(?P<answer_id>\d+)/$', views.check_answer)
    )
