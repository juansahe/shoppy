# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from games.views import *

urlpatterns = [
    url(r'^task/$',TaskList.as_view(), name='task'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
