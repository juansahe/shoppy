from django.contrib import admin

from .models import Provider,Promotion



class ProviderAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name')

    def image_tag(self, obj):
        return u'<img src="%s" width="50px"/>' % (obj.img.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

admin.site.register(Provider,ProviderAdmin)
admin.site.register(Promotion)
