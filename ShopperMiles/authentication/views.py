# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# from django.core.mail import EmailMessage
# from django.template import Context
# from django.template.loader import get_template
# from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken as ObtainToken
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
# from common.tasks import send_email
from users.models import User
from .serializers import AuthTokenSerializer
import json

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # userss =json.dumps(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': token.user_id})

# def send_new_password_mail(user, password, forgotten=False):
    # """
    # Send a html message email
    # """
    # subject = 'Has olvidado tu contraseña' if forgotten else 'Tu contraseña ha sido modificada'
    # send_email.delay(
            # subject,
            # [user.email],                    #recipients
            # {
                # 'user': user,
                # 'raw_password': password,
                # 'forgotten': forgotten
                # },
            # 'emails/new_password.html'
            # )

    # @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def reset_my_password(request):
    # """
    # change your password
    # """
    # old_password = request.data.get('old_password', None)
    # password = request.data.get('password', None)
    # password_confirm = request.data.get('password_confirm', None)

    # if old_password and password and password_confirm and \
            # password == password_confirm:

                # user = request.user
        # if user.check_password(old_password):
            # user.set_password(password);
            # user.save()
            # return Response(
                    # {"message" : "ok"},
                    # status=status.HTTP_204_NO_CONTENT
                    # )
        # else:
            # return Response(
                    # {"error" : "current password do not match"},
                    # status=status.HTTP_400_BAD_REQUEST
                    # )
    # else:
        # return Response(
                # {"error" : "the passwords do not match"},
                # status=status.HTTP_400_BAD_REQUEST
                # )

        # @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def reset_password(request, pk=None):
    # """
    # Set a new password. This view is for superadmin, admin, subadmins.
    # A email will be send
    # """
    # password = request.data.get('password', None)
    # password_confirm = request.data.get('password_confirm', None)
    # user = User.objects.get(pk=pk)

    # if request.user.is_superuser is True or \
            # (request.user.is_superuser is False and  \
            # request.user.role in ['ADMIN', 'SUBADMIN'] and \
            # request.user.company==user.company):

                # if password and password_confirm and password == password_confirm:
                    # user.set_password(password)
            # user.save()
            # send_new_password_mail(user, password)

            # return Response(
                    # {"message" : "ok"},
                    # status=status.HTTP_204_NO_CONTENT
                    # )
        # else:
            # return Response(
                    # {"error" : "the passwords do not match", "lang": "en"},
                    # status=status.HTTP_400_BAD_REQUEST
                    # )
    # else:
        # return Response(
                # {"error" : "Forbbiden"},
                # status=status.HTTP_403_FORBIDDEN
                # )

        # @api_view(['POST'])
# @permission_classes([AllowAny])
# def forgotten_password(request):
    # """
    # Set and send a random password.
    # """
    # email = request.data.get('email', None)
    # if not email:
        # return Response({"error" : "need a email"}, status=status.HTTP_400_BAD_REQUEST)
    # else:
        # user = get_object_or_404(User, email=email)
        # password = User.objects.make_random_password()
        # user.set_password(password)
        # user.save()
        # send_new_password_mail(user, password, True)
        # return Response({"message" : "ok"}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def check_email(request):
    # """
    # Check if the email exists
    # """
    # email = request.data.get('email', None)
    # if not User.objects.filter(email=email):
        # return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    # else:
        # return Response({'message': 'fail'}, status=status.HTTP_200_OK)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def check_username(request):
    # """
    # Check if the username exists
    # """
    # username = request.data.get('username', None)
    # if not User.objects.filter(username=username):
        # return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    # else:
        # return Response({'message': 'fail'}, status=status.HTTP_200_OK)

# class DestroyTokenView(generics.DestroyAPIView):
    # """
    # logout: eliminate the token of current user
    # """
    # queryset = Token.objects.all()
    # permission_classes= (IsAuthenticated,)

    # def get_object(self):
        # return self.queryset.get(user=self.request.user)
