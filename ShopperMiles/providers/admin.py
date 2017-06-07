from django.contrib import admin

from .models import Mark,Retail



class MarkAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name')

    def image_tag(self, obj):
        return u'<img src="%s" width="50px"/>' % (obj.img.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class RetailAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name')

    def image_tag(self, obj):
        return u'<img src="%s" width="50px"/>' % (obj.img.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


admin.site.register(Mark,MarkAdmin)
admin.site.register(Retail,RetailAdmin)