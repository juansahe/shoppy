from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from products.views import *

urlpatterns = [
    url(r'^product/$', ProductList.as_view(), name='product'),
    url(r'^category/$',CategoryList.as_view(), name='category'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
