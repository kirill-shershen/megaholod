from django.conf.urls import *
from news.views import block_news, news

urlpatterns = patterns('',
    url(r'^$', news, name='news'),
)