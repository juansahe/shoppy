# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        queryset = self.get_queryset()
        self.serializer_class = TaskSerializer
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
