# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class News(models.Model):
    """docstring for News"""
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text  = models.TextField(verbose_name='текст')
    time  = models.DateTimeField(auto_now_add=True, verbose_name='время')

    class Meta:
        ordering = ['-time']
        verbose_name = 'Новость'
        verbose_name_plural = 'новости'
            
    def __unicode__(self):
        return self.title
        