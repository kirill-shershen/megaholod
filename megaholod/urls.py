from django.conf.urls import patterns, include, url
from filebrowser.sites import site
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings
from megaholod import views
from django.views.generic import DetailView
from product.models import Object
from product.views import objs

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'megaholod.views.index', name='index'),
    url(r'^contacts/', include('feedback.urls'), name='contacts'),
    url(r'^news/', include('news.urls'), name='news'),
    url(r'^about/', views.flat_page, name='about'),
    url(r'^product/', include('product.urls'), name='windows'),
    url(r'^news/', include('news.urls'), name='news'),
    url(r'^objects/$', objs, name='objects'),
    url(r'^objects/(?P<pk>\d+)$', DetailView.as_view(model=Object, template_name='object_detail.html')),
    url(r'^carbon-filter/$', views.flat_page, name='carbon-filter'),
    url(r'^furneture/$', views.furneture, name='furneture'),
    url(r'^lamination/$', views.flat_page, name='lamination'),
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