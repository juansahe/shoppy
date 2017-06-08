from django.contrib import admin

from django.contrib import admin

from .models import Task



class TaskAdmin(admin.ModelAdmin):
    list_display = ('point_exp',)


admin.site.register(Task,TaskAdmin)
