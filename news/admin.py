from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from megaholod import settings
from news.models import News
class CollectionAdmin(admin.ModelAdmin):
 
    class Media:
        js = (
            '%stinymce/tiny_mce.js' % settings.STATIC_URL, 
            '%stinymce/tiny_mce_init.js' % settings.STATIC_URL,
        )

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CollectionAdmin)
admin.site.register(News, CollectionAdmin)