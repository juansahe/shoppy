# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
# from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Token authentication
    url(
        r'^token/',
        views.ObtainAuthToken.as_view()
    ),
    url(
        r'^register/',
        views.UserRegister.as_view()
    ),

    # url(
    # r'^exit/',
    # views.DestroyTokenView.as_view()
    # ),
    # url(
    # r'^(?P<pk>[0-9]+)/reset_password/$',
    # views.reset_password,
    # name="user-reset-password"
    # ),
    # url(register
    # r'^reset_my_password/$',
    # views.reset_my_password,
    # name="user-reset-my-password"
    # ),
    # url(
    # r'^forgotten_password/$',
    # views.forgotten_password,
    # name="user-forgotten-password"
    # ),
    # url(
    # r'^check_email/$',
    # views.check_email,
    # name="user-check-email"
    # ),
    # url(
    # r'^check_username/$',
    # views.check_username,
    # name="user-check-username"
    # ),
    # # browsable API
    # url(
    # r'',
    # include(
    # 'rest_framework.urls',
    # namespace='rest_framework'
    # )
    # ),
]
