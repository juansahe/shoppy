from __future__ import unicode_literals, absolute_import

from django.db import models

class Task(models.Model):
    # additional fields here
    level = (
    ('bro', 'Bronce'),
    ('pla', 'Plata'),
    ('oro', 'Oro'),
)

    name =  models.CharField( verbose_name="Titulo de la  tarea",max_length=255)
    type_task =  models.CharField( verbose_name=" Tipo de tarea",max_length=20,choices=level,default='bro',)
    point_exp = models.IntegerField(verbose_name="Experiencia de la tarea",)
    SM = models.IntegerField(verbose_name="Puntos SM de esta tarea")
    def __str__(self):
        return self.type_task

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['pk']

