# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from apps.misc import views as misc_view
from apps.news import views as news_view
from apps.sponsor import views as sponsor_view

urlpatterns = [
    # Django
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Apps
    url(r'^api/', include('apps.api.urls')),
    url(r'^arrivals/', include('apps.arrivals.urls')),
    url(r'^auth/', include('apps.authentication.urls')),
    url(r'^competition/', include('apps.competition.urls')),
    url(r'^lan/', include('apps.lan.urls')),
    url(r'^lottery/', include('apps.lottery.urls')),
    url(r'^news/', include('apps.news.urls')),
    url(r'^payment/', include('apps.payment.urls')),
    url(r'^profile/', include('apps.userprofile.urls')),
    url(r'^team/', include('apps.team.urls')),
    url(r'^seating/', include('apps.seating.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman')),

    # Views
    url(r'^$', news_view.main, name='root', kwargs={'page': 1}),
    url(r'^misc/remove_alert.html$', misc_view.remove_alert),
    url(r'^misc/change_language$', misc_view.change_language),
    url(r'^sponsors/', sponsor_view.index, name='sponsors'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^404$', misc_view.handler404, name='404_handler'),
        url(r'^500$', misc_view.handler500, name='500_handler'),
    ]

handler404 = 'apps.misc.views.handler404'
handler500 = 'apps.misc.views.handler500'
