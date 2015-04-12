# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^login/$', 'teams.views.do_login', name="login"),
                       url(r'^logout/$', 'teams.views.do_logout', name="logout"),
                       url(r'^show/(.*)/$', 'teams.views.show'),
                       url(r'^lang/(..)/$', 'teams.views.set_lang', name='set_lang')
)
