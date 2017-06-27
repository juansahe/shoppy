# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from rest_framework import generics
from .models import Product
from .models import Category
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self):
        queryset = self.get_queryset()
        self.serializer_class = CategorySerializer
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        queryset = self.get_queryset()
        self.serializer_class = ProductSerializer
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

"""
-------------------------------------------------------------------------
    Rather than writing your own viewsets, you'll often want to use
    the existing base classes that provide a default set of behavior.
-------------------------------------------------------------------------
Example:

class UserViewSet(viewsets.ModelViewSet):
    #A viewset for viewing and editing user instances.

    serializer_class = UserSerializer
    queryset = User.objects.all()
"""
