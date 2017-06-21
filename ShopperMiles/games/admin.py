from django.contrib import admin

from django.contrib import admin

from .models import Task,Level



class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('number','point_xp','point_sm',)


admin.site.register(Task,TaskAdmin)
admin.site.register(Level,LevelAdmin)
