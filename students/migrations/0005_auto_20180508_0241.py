# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-08 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20180508_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='khmer_salary',
            field=models.FloatField(blank=True, default=150, max_length=10),
        ),
    ]
