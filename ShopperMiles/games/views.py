# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Task, Level
from favorites.models import Favorite
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
import json
from django.core import serializers
from users.models import User,Redemption,User_Task
from providers.models import Bond


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


class UserTask(View):

    def get(self, request):
        pass

    def post(self, request):
        # data = json.loads(request.body)
        ctx = {}
        favs = []
        data = json.loads(request.body)
        user = User.objects.get(pk=data['id'])
        user_task = User_Task.objects.filter(user_id=user.id)
        print user_task
        # if user == 
        serialized_obj = serializers.serialize('json', user_task,)
        objectall1 = json.loads(serialized_obj)
        favorites = Favorite.objects.filter(user=data['id'])
        for fav in favorites:
            favs.append(fav.product_id)


        tasking = Task.objects.filter(
            product_id__in=favs, level_id=user.level_id)
        serialized_obj = serializers.serialize('json', tasking,)
        objectall = json.loads(serialized_obj)
        # return render(request, 'client_profile.html', ctx)
        # ctx['error'] = user_task
        # return JsonResponse(objectall1,objectall,safe=False)
        # return JsonResponse(objectall,safe=False)
        ctx['msg'] = objectall
        ctx['tareacompletada'] = objectall1
        return JsonResponse(ctx, safe=False)

class RedemptionBond(View):

    def get(self, request):
        pass

    def post(self, request):

        ctx = {}
        us = []
        data = json.loads(request.body)
        # print data
        user = User.objects.get(pk=data['user_id'])
        bond = Bond.objects.get(pk=data['bond_id'])
        # print user
        # print bond

        if user.shopper_points >= bond.shopy_value:

            new_register = Redemption(
                bond_id=data['bond_id'],
                user_id=data['user_id'],
                name=data['name'],
                code=data['code'],
                description=data['description'],
                imagen=data['imagen'],
                value=data['value'],
            )

            ctx['msg'] = "se guardo con exito"
            new_register.save()
            return JsonResponse(ctx, safe=False)

        else:
            ctx['error'] = "No le alcanza"
            return JsonResponse(ctx, safe=False)


class Mybond(View):

    def get(self, request):
        pass

    def post(self, request):
        ctx = {}
        data = json.loads(request.body)
        # print data
        # queryset = Bond.objects.prefetch_related(
        #     'redemption_set'
        # ).filter(pk = data['user_id'])

        bonds= Redemption.objects.prefetch_related().filter(user_id=data['user_id'])
        # bonds.entry__set.all()
        serialized_obj = serializers.serialize('json', bonds,)
        objectall = json.loads(serialized_obj)
        ctx['msg'] = "se guardo con exito"
        ctx['bonos'] = objectall
        return JsonResponse(ctx, safe=False)



        


"""
-------------------------------------------------------------------------
    Rather than writing your own viewsets, you'll often want to use
    the existing base classes that provide a default set of behavior.
-------------------------------------------------------------------------
Example:

class UserViewSet(viewsets.ModelViewSet):
    # A viewset for viewing and editing user instances.

    serializer_class = UserSerializer
    queryset = User.objects.all()
"""
