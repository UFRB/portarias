# -*- coding: utf-8 -*-
#
#  Copyright (c) 2014 Wille Marcel Lima Malheiro and contributors
#
#  This file is part of Portaria.
#
#  Portaria is free software under terms of the GNU Affero General Public
#  License version 3 (AGPLv3) as published by the Free
#  Software Foundation. See the file README for copying conditions.
#

from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url

from .views import Index, Search, Relatorio, ExportarPortarias


urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^relatorio/$',
         login_required(Relatorio.as_view(), login_url='/admin/'),
         name='relatorio'),
    url(r'page(?P<page>[0-9]+)/^$', Index.as_view(), name='index'),
    url(r'^busca/$', Search.as_view()),
    url(r'^exportar/$',
        login_required(ExportarPortarias, login_url='/admin/'),
        name='exportar'),
)