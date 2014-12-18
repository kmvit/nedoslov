# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='price',
            field=models.IntegerField(default=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='carousel',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
