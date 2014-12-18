# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
# Create your models here.

class Carousel(models.Model):
    name = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='afisha')
    data = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0,blank=True)
    content = tinymce_models.HTMLField(verbose_name=u'Описание',blank=True)

    class Meta:
        verbose_name = u'Карусель афиш'
        verbose_name_plural = u'Добавить афишу'
        
    def __unicode__(self):
        return self.name

    
class Headermenu(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url = models.CharField(max_length=256, unique=True)

    class Meta:
        verbose_name = u'Меню'
        verbose_name_plural = u'Добавить меню'
        
    def __unicode__(self):
        return self.name
