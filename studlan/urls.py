# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'studlan.news.views.main', name='root', kwargs={'page': 1}),
    url(r'^login.html', 'studlan.competition.views.log_in'),
    url(r'^logout.html', 'studlan.competition.views.log_out'),
    url(r'^register.html', 'studlan.competition.views.register_user'),
    url(r'^misc/remove_alert.html', 'studlan.misc.views.remove_alert'),

    # app urls
    url(r'^api/',           include('studlan.api.urls')),
    url(r'^arrivals/',      include('studlan.arrivals.urls')),
    url(r'^auth/',          include('studlan.authentication.urls')),
    url(r'^competition/',   include('studlan.competition.urls')),
    url(r'^lan/',           include('studlan.lan.urls')),
    url(r'^news/',          include('studlan.news.urls')),
    url(r'^profile/',       include('studlan.userprofile.urls')),
    url(r'^team/',          include('studlan.team.urls')),
    url(r'^lottery/',       include('studlan.lottery.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'studlan.misc.views.handler404'
