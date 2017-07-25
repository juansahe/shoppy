# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users.views import *

urlpatterns = [

	
    # url(r'^redemption/$', Redemption.as_view(), name='redemption'),
    # url(r'^redemptionBond/$', RedemptionBond.as_view(), name='redemptionBond'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
