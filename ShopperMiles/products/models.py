# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible

class Product(models.Model):
    # additional fields here
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    img = models.ImageField(upload_to = 'uploads/')
    def __str__(self):
        return self.name
