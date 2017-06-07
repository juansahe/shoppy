from __future__ import unicode_literals, absolute_import

from django.db import models

class Task(models.Model):
    # additional fields here
    level = (
    ('bro', 'Bronce'),
    ('pla', 'Plata'),
    ('oro', 'Oro'),
)

    type_task =  models.CharField(max_length=20,choices=level)
    point_exp = models.IntegerField()
    SM = models.IntegerField()
    def __str__(self):
        return self.type_task


class Level(models.Model):
    # additional fields here
    number = models.IntegerField()
    point = models.IntegerField()
    def __str__(self):
        return self.number
