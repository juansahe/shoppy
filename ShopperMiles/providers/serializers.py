
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from rest_framework import serializers
from .models import Promotion,Provider,Bond

class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ('id', 'name', 'description' , 'img','provider')

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id','type_provider', 'name', 'description','phone_contact','name_contact','email_contact','img','web_site')

class BondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bond
        fields = ('id', 'name', 'description' ,'value1','value2','value3','code','status','provider','img')

