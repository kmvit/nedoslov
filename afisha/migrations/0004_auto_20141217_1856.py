# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0003_auto_20141217_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headermenu',
            options={'verbose_name': '\u041c\u0435\u043d\u044e', 'verbose_name_plural': '\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0435\u043d\u044e'},
        ),
        migrations.AddField(
            model_name='carousel',
            name='content',
            field=tinymce.models.HTMLField(default=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carousel',
            name='poster',
            field=models.ImageField(upload_to=b'afisha'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carousel',
            name='price',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
