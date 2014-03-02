# -*- coding: utf-8 -*-
from django.db import models

class Product(models.Model):
    category_type = (
        ('WD', 'Окна'),
        ('HV', 'Пылесосы')
    )

    category = models.CharField(max_length=2, choices=category_type)
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='uploads')
    description = models.TextField(max_length = 500)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'продукты'

    def get_absolute_url(self):
        return '/windows/%i'% self.id

class Object(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='uploads', verbose_name='картинка')
    date = models.DateTimeField(verbose_name='дата')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-date']
        verbose_name = 'Объект'
        verbose_name_plural = 'объекты'