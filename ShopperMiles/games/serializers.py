# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name', 'type_task', 'point_exp', 'SM', 'level',
                'product', 'pregunta', 'respuesta','imagen')
        # read_only_fields = ('name', 'auth_token', 'date_joined',)

