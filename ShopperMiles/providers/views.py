# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.shortcuts import render
from rest_framework import generics
from .models import Promotion
from .serializers import PromotionSerializer
from .models import Provider
from .serializers import ProviderSerializer
from .models import Bond
from users.models import User_Task, User
from games.models import Task, Level
from .serializers import BondSerializer
from django.views.generic import View
from django.http import JsonResponse
import json
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


class saveTask(View):

    def get(self, request):
        pass

    def post(self, request):

        ctx = {}
        data = json.loads(request.body)
        user = User.objects.get(pk=data['user_id'])
        # print user.level_id
        level = Level.objects.get(pk=user.level_id)
        # print level.point_xp
        point_user = user.shopper_points
        # print point_user
        task = Task.objects.get(pk=data['tarea_id'])
        point_task = task. point_exp
        # print point_task
        total_point = int(point_user) + int(point_task)
        total_xp = int(task.point_exp) + int(user.xperience)
        # print total_point
        print level.point_xp
        print user.xperience

        if int(user.xperience) >= int(level.point_xp):
            levelUpgrade = Level.objects.filter(
                number=level.number + 1).exists()

            # print levelUpgrade.count()
            print levelUpgrade
            if levelUpgrade:
                levelUpgrade = Level.objects.get(number=level.number + 1)

                User.objects.filter(pk=data['user_id']).update(
                    level_id=levelUpgrade.id, shopper_points=total_point, xperience=total_xp)
                new_register = User_Task(

                    state=data['state'],
                    user_id=data['user_id'],
                    tarea_id=data['tarea_id'],

                )
                new_register.save()
                ctx['msg'] = "se guardo con exito"
                return JsonResponse(ctx, safe=False)
            else:
                User.objects.filter(pk=data['user_id']).update(
                    shopper_points=total_point, xperience=total_xp)
                new_register = User_Task(

                    state=data['state'],
                    user_id=data['user_id'],
                    tarea_id=data['tarea_id'],

                )
                new_register.save()
                ctx['msg'] = "se guardo con exito"
                return JsonResponse(ctx, safe=False)

        else:

            User.objects.filter(pk=data['user_id']).update(
                shopper_points=total_point, xperience=total_xp)
            new_register = User_Task(

                state=data['state'],
                user_id=data['user_id'],
                tarea_id=data['tarea_id'],

            )
            new_register.save()
            ctx['msg'] = "se guardo con exito"
            return JsonResponse(ctx, safe=False)

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
