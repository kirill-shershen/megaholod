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
