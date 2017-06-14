# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
#from versatileimagefield.fields import VersatileImageField
from datetime import datetime

from games.models import Level

@python_2_unicode_compatible

class User(AbstractUser):
    # additional fields here
    xperience = models.CharField(max_length=100,null=True ,default="0")
    shopper_points = models.CharField(max_length=100,null=True,default="0")
    bornday = models.DateField(null=True)
    level = models.OneToOneField(
        Level,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True,
        )

    def __str__(self):
        return self.username


# for time spamped models
