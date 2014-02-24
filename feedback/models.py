# -*- coding:utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Feedback(models.Model):
    """
    feedback model, ordering set to time desc
    default table name changed to 'feedbacks'
    """
    class Meta:
        ordering = ['-time']
        db_table = 'feedbacks'
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'фидбэки'

    name   = models.CharField(max_length=100, verbose_name= 'имя')
    email   = models.EmailField(verbose_name= 'почта')
    phone   = models.CharField( max_length=100, verbose_name='телефон')
    message = models.TextField(max_length=500, verbose_name='сообщение')
    time    = models.DateTimeField(auto_now_add=True, verbose_name='время')

    def __unicode__(self):
        return '%s(%s)'%(self.name, self.phone)

    # def get_absolute_url(self):
    #     return reverse('admin:view-feedback', args=[self.id])