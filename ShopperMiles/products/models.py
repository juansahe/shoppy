# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models


class Product(models.Model):
    # additional fields here
    xperience = models.CharField(max_length=100,null=True)
    shopper_points = models.CharField(max_length=100,null=True)
    bornday = models.DateField(null=True)
    def __str__(self):
        return self.username


