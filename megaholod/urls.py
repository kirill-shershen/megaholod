from django.conf.urls import patterns, include, url
from filebrowser.sites import site
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings
from megaholod import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'megaholod.views.index', name='index'),
    url(r'^contacts/', 'megaholod.views.contacts', name='contacts'),
    # url(r'^megaholod/', include('megaholod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))