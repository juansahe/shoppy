# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
#from versatileimagefield.fields import VersatileImageField
from datetime import datetime

from games.models import Level, Task

# from providers.models import Bond

# from games.models import Task

# from common.models import TimeStampedModel


@python_2_unicode_compatible
class User(AbstractUser):
    # additional fields here
    xperience = models.CharField(max_length=100, null=True, default="0")
    shopper_points = models.CharField(max_length=100, null=True, default="0")
    bornday = models.DateField(null=True)
    level = models.OneToOneField(
        Level,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True,
    )

    def __str__(self):
        return str(self.pk)


# class Redemption(models.Model):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=False,
#         verbose_name="Usuario"
#     )

#     bond = models.ForeignKey(
#         Bond,
#         on_delete=models.CASCADE,
#         primary_key=False,
#         verbose_name="Bonos"
#     )

#     def __str__(self):
#         return self.user

#     class Meta:
#         verbose_name = "Redencion"
#         verbose_name_plural = "Redenciones"
#         ordering = ['user']


class User_Task(models.Model):

    state = (
        ('Com', 'Completa'),
        ('Inc', 'Incompleta'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        verbose_name="Usuario"
    )

    tarea = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        primary_key=False,
        verbose_name="Tareas"
    )

    state = models.CharField(
        max_length=100, verbose_name="Estado de la tarea", choices=state, default='Com',)

    def __str__(self):
        return self.state


# for time spamped models
