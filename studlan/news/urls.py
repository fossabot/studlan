# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('studlan.news.views',
    url(r'^$', 'main', name='news_main', kwargs={'page': 1}),
    url(r'^(?P<page>\d+)/$', 'main', name='news'),
)
