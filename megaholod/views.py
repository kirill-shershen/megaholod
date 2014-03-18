from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage

cust_templs = ['contacts', 'furneture', 'lamination']


def flat_page(request, templ='flat_page'):
    flatpage = FlatPage.objects.get(url='/%s/' % templ)
    if templ in cust_templs:
        templ_name = templ
    else:
        templ_name = 'flat_page'
    return render(request, '%s.html' % templ_name, locals())


def contacts(request):
    contacts = FlatPage.objects.get(url=request.path)
    return render(request, 'contacts.html', locals())


def about(request):
    about = FlatPage.objects.get(url=request.path)
    return render(request, 'about.html', locals())


def index(request):
    return render(request, 'index.html', locals())
