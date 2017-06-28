# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.shortcuts import render
from rest_framework import generics
from .models import Promotion
from .serializers import PromotionSerializer
from .models import Provider
from .serializers import ProviderSerializer
from .models import Bond
from .serializers import BondSerializer
from django.shortcuts import get_object_or_404

class PromotionList(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

    def get_object(self):
        queryset = self.get_queryset()
        self.serializer_class = PromotionSerializer
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def get_object(self):
        queryset = self.get_queryset()
        self.serializer_class = ProviderSerializer
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class BondList(generics.ListCreateAPIView):
    queryset = Bond.objects.all()
    serializer_class = BondSerializer

    def get_object(self):
        queryset = self.get_queryset()
        self.serializer_class = BondSerializer
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

