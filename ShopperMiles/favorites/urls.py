# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from favorites.views import *

urlpatterns = [
    url(r'^favorite/$', FavoriteList.as_view(), name='favorite'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
