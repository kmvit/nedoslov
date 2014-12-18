# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u0418\u043c\u044f')),
                ('portret', models.ImageField(upload_to=b'actor', verbose_name='\u041f\u043e\u0440\u0442\u0440\u0435\u0442')),
                ('content', tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0410\u043a\u0442\u0435\u0440\u044b',
                'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u043a\u0442\u0435\u0440\u0430',
            },
            bases=(models.Model,),
        ),
    ]
