# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0004_auto_20141217_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
    ]
