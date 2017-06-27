# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.contrib import admin


from .models import  Favorite



class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('product','user',)




admin.site.register(Favorite,FavoriteAdmin)



