# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from .models import Mensaje

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('name','mensaje',)

admin.site.register(Mensaje,MensajeAdmin)


