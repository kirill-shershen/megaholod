from django.shortcuts import render, redirect
from django.contrib.flatpages.models import FlatPage

def index(request):
    return render(request, 'index.html', locals())

def contacts(request):
    contacts = FlatPage.objects.get(url=request.path)
    return render(request, 'contacts.html', locals())