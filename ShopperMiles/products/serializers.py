# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'img')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'img', 'category', 'provider')


# class CreateProductSerializer(serializers.ModelSerializer):
#     # is_active = serializers.BooleanField(default=True)

#     def create(self, validated_data):
#         # call create_user on user object. Without this
#         # the password will be stored in plain text.
#         # user = User.objects.create_user(**validated_data)
#         product = Product.objects.create(
#                  name=validated_data['name'],
#                  description=validated_data['description'],
#                  img=validated_data['img'],
#                  category_id=validated_data['category_id'],
#                  provider_id=validated_data['provider_id'],
#         )
#         return product

#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'img',
#                 'category_id', 'provider_id')
    # read_only_fields = ('auth_token',)
