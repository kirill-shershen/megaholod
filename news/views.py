from django.shortcuts import render
from news.models import News
# Create your views here.
def block_news(request):
    last_news = News.objects.all()[-2]
    return render(request, "block_news.html", locals())

def news(request):
    last_news = News.objects.all()[-2]
    return render(request, "news.html", locals())