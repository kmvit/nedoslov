# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0002_auto_20141217_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headermenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('url', models.CharField(unique=True, max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='poster',
            field=models.ImageField(upload_to=b'afisha', blank=True),
            preserve_default=True,
        ),
    ]
