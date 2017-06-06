from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name','description',)

    def image_tag(self, obj):
        return u'<img src="%s" width="50px"/>' % (obj.img.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

admin.site.register(Product,ProductAdmin)
