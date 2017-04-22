# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0003_factura_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='cedula',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='sede',
            name='cedula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]
