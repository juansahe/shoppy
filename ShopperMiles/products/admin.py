from django.contrib import admin

from .models import Product,Category



class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name','description',)

    def image_tag(self, obj):
        return u'<img src="%s" width="50px"/>' % (obj.img.url)
    image_tag.short_description = 'Imagen del producto'
    image_tag.allow_tags = True

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','name')

    def image_tag(self, obj):
        return u'<img src="%s" width="50px"/>' % (obj.img.url)
    image_tag.short_description = 'Imagen'
    image_tag.allow_tags = True




admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)


