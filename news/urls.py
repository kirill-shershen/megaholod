from django.conf.urls import *
from news.views import block_news, news
from news.models import News
from news.views import NewsListView

urlpatterns = patterns('',
    url(r'^$', NewsListView.as_view(queryset=News.objects.all(), template_name='news.html')),
)