# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models

class Product(models.Model):
    # additional fields here
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    img = models.ImageField(upload_to = 'uploads/products/')
    def __str__(self):
        return self.name


class Category(models.Model):
    # additional fields here
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'uploads/category/')
    def __str__(self):
        return self.name