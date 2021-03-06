# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework import generics
from rest_framework import parsers, renderers
from .permissions import IsOwnerOrReadOnly, IsAdminOrIsSelf
from .serializers import CreateUserSerializer, UserSerializer
from providers.models import Bond
from django.http import JsonResponse
import json
from django.core import serializers
from .serializers import RedemptionSerializer
from users.models import User,User_Task
from django.views.generic import View


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, retrives and delete User accounts
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_fields = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                     'is_superuser', 'is_active',)

    # def post(self, request):
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     if user.is_active:
    #         login(request , user)
    # return redirect('')

    def list(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated,)
        query = self.request.query_params.get('with_deleted', None)
        if query is not None:
            self.queryset = User.objects.all()
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (IsAuthenticated,)
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsAdminOrIsSelf,)
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        self.permission_classes = (IsAdminOrIsSelf,)
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf, ])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('password', None)
        password_confirm = request.data.get('password_confirm', None)

        if new_password and password_confirm and new_password == password_confirm:
            user.set_password(new_password)
            user.save()
            return Response({"message": "ok"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "the passwords do not match"},
                            status=status.HTTP_400_BAD_REQUEST)



# class Redemption(generics.ListCreateAPIView):
#     queryset = Redemption.objects.all()
#     serializer_class = RedemptionSerializer

#     def get_object(self):
#         queryset = self.get_queryset()
#         self.serializer_class = RedemptionSerializer
#         obj = get_object_or_404(
#             queryset,
#             pk=self.kwargs['pk'],
#         )
#         return obj



        # ctx["id"] = new_register.id

        # data = json.loads(request.body)
        # user = User.objects.get(pk=data['id'])
        # bond = Bond.objects.get(pk=data['id'])
        # print user
        # print bond
        # ctx = {}
        # ctx['error'] = "no se existe"
        # return JsonResponse(ctx, safe=False)
#         tasking = Task.objects.filter(product_id__in=favs, level_id=user.level_id )
#         serialized_obj = serializers.serialize('json', tasking,)
#         objectall = json.loads(serialized_obj)

#         # return render(request, 'client_profile.html', ctx)
#         return JsonResponse(objectall, safe=False)

        # if (data.User.objects.get(email=data['email']))
        # print
        # try:
        #     renden = User.objects.get(
        #         id=data['id'])
        #     ctx['error'] = "no se existe"
        #     return JsonResponse(ctx, safe=False)

        # except ObjectDoesNotExist:

        #     ctx['succes'] = "Guardado con exito"
        #     # # se crea una nueva direccion
        #     new_register = Redemption(
        #         username=data['email'],
        #         first_name=data['username'],
        #         email=data['email'],
        #         bornday=data['bornday'],
        #         password=make_password(data['password']),
        #     )
        #     new_register.save()
        #     ctx["id"] = new_register.id
        #     token, created = Token.objects.get_or_create(user=new_register)
        #     ctx["token"] = token.key
        #     return JsonResponse(ctx, safe=False)

        # except MultipleObjectsReturned as e:
        #     ctx['error'] = "no se pudo registrar el usuario ya existe"
        #     return JsonResponse(ctx, safe=False)

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
