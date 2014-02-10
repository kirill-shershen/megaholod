from django.contrib import admin
from megaholod import settings
from product.models import Product

class CollectionAdmin(admin.ModelAdmin):
 
    class Media:
        js = (
            '%stinymce/tiny_mce.js' % settings.STATIC_URL, 
            '%stinymce/tiny_mce_init.js' % settings.STATIC_URL,
        )

admin.site.register(Product, CollectionAdmin)