# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('poster', models.ImageField(upload_to=b'/afisha/', blank=True)),
                ('data', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0443\u0441\u0435\u043b\u044c \u0430\u0444\u0438\u0448',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0444\u0438\u0448\u0443',
            },
            bases=(models.Model,),
        ),
    ]
