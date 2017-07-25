# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from games.views import *
# from users.views import *

urlpatterns = [
    url(r'^task/$', UserTask.as_view(), name='save_task'),
    url(r'^save_task/$', TaskList.as_view(), name='task'),
    url(r'^redemptionBond/$', RedemptionBond.as_view(), name='redemptionBond'),
    url(r'^Mybond/$', Mybond.as_view(), name='Mybond'),
    


]

urlpatterns = format_suffix_patterns(urlpatterns)
