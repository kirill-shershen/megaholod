from django.shortcuts import render, redirect
from django.contrib.flatpages.models import FlatPage

def flat_page(request):
    flatpage = FlatPage.objects.get(url=request.path)
    return render(request, 'flat_page.html', locals())

def index(request):
    return render(request, 'index.html', locals())

def contacts(request):
    contacts = FlatPage.objects.get(url=request.path)
    return render(request, 'contacts.html', locals())

def furneture(request):
    furneture = FlatPage.objects.get(url=request.path)
    return render(request, 'furneture.html', locals())