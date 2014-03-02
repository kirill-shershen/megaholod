from django.conf.urls import *
from product.views import windows, vacs
from product.models import Product  
from django.views.generic import DetailView

urlpatterns = patterns('',
    url(r'^$', windows, name='windows'),
    url(r'^windows/$', windows, name='windows'),
    url(r'^vacs/$', vacs, name='vacs'),
    url(r'^windows/(?P<pk>\d+)$', DetailView.as_view(model=Product, template_name='product_detail.html')),
    url(r'^vacs/(?P<pk>\d+)$', DetailView.as_view(model=Product, template_name='product_detail.html')),
)