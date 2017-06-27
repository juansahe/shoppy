# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from providers.views import *

urlpatterns = [
    url(r'^promotion/$', PromotionList.as_view(), name='promotion'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
