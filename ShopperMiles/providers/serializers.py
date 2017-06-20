
from __future__ import absolute_import, unicode_literals
from rest_framework import serializers
from .models import Promotion

class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ('id', 'name', 'description' , 'img','provider')
