from django.shortcuts import render

from rest_framework import generics
from .models import Favorite
from .serializers import FavoriteSerializer
from django.shortcuts import get_object_or_404

class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_object(self):
        queryset = self.get_queryset()
        self.serializer_class = FavoriteSerializer
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
