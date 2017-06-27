# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include, url
from django.contrib import admin
from django.views import defaults
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/auth/login', include('rest_framework.urls',namespace='rest_framework')),

    # Main
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    # REST-API
    url(r'^api/', include('products.urls', namespace='products')),
    url(r'^api/', include('favorites.urls', namespace='favorites')),
    url(r'^api/', include('providers.urls', namespace='providers')),
    url(r'^api/', include('games.urls', namespace='games')),
    url(r'^api/', include('authentication.urls')),
    url(r'^api/', include(router.urls)),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', defaults.bad_request),
        url(r'^403/$', defaults.permission_denied),
        url(r'^404/$', defaults.page_not_found),
        url(r'^500/$', defaults.server_error),
    ]
    # static/media files
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += [
        url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework'))
    ]
