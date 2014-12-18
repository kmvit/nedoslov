# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='slug',
            field=models.SlugField(default=True, unique=True),
            preserve_default=True,
        ),
    ]
