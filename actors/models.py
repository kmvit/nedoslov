# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class Actors(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'Имя')
    slug = models.SlugField(unique=True)
    portret = models.ImageField(upload_to='actor',verbose_name=u'Портрет')
    content = tinymce_models.HTMLField(verbose_name=u'Описание',blank=True)

    class Meta:
        verbose_name = u'Актеры'
        verbose_name_plural = u'Добавить актера'
        
    def __unicode__(self):
        return self.name
