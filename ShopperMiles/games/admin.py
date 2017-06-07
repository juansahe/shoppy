from django.contrib import admin

from django.contrib import admin

from .models import Task,Level



class TaskAdmin(admin.ModelAdmin):
    list_display = ('point_exp',)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('number',)

admin.site.register(Task,TaskAdmin)
admin.site.register(Level,LevelAdmin)
