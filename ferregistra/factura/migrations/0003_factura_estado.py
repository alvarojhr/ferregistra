# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_auto_20170415_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='estado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
