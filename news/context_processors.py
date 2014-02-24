from news.models import News

def get_lastnews(request):
    ln = News.objects.all()[:2]

    return {'last_news': ln} 