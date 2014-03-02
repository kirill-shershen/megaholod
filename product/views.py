# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from product.models import Product, Object

def windows(request):
    windows = Product.objects.filter(category = 'WD')
    # делаем плитку из массива кортежей по 3 записи
    kort = []
    i=1
    recs = []
    for rec in windows:
        if i % 3 == 0:
            recs.append(rec)
            kort.append(tuple(recs))
            recs = []
        else:
            recs.append(rec)
            if i == len(windows):
                kort.append(tuple(recs))
        i += 1

    return render(request, 'windows_list.html', locals())

def vacs(request):
    vacs = Product.objects.filter(category = 'HV')
    # делаем плитку из массива кортежей по 3 записи
    kort = []
    i=1
    recs = []
    for rec in vacs:
        if i % 3 == 0:
            recs.append(rec)
            kort.append(tuple(recs))
            recs = []
        else:
            recs.append(rec)
            if i == len(vacs):
                kort.append(tuple(recs))
        i += 1
    return render(request, 'vac_list.html', locals())

def objs(request):
    objs = Object.objects.all()
    return render(request, 'object_list.html', locals())