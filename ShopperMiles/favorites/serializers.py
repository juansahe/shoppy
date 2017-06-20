from __future__ import absolute_import, unicode_literals
from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('id', 'product', 'user')
