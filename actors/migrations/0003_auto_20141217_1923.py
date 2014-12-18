# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_actors_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
