from django.conf.urls import *
from product.views import windows, vacs

urlpatterns = patterns('',
    url(r'^$', windows, name='windows'),
    url(r'^windows/', windows, name='windows'),
    url(r'^vacs/', vacs, name='vacs'),
)