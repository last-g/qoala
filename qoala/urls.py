# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qoala.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'board.views.task_board', name="home"),
    url(r'^board/', include('board.urls')),
    url(r'^tasks/', include('quests.urls')),
    url(r'^teams/', include('teams.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
