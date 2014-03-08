from django.conf.urls import *
from news.views import block_news, news
from news.models import News
from news.views import NewsListView
from django.views.generic import DetailView

urlpatterns = patterns('',
    url(r'^$', NewsListView.as_view(queryset=News.objects.all(), template_name='news_list.html')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=News, template_name='news_detail.html')),
)