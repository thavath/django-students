# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-08 02:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20180508_0225'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendace',
            new_name='Attendance',
        ),
        migrations.RemoveField(
            model_name='academic',
            name='student',
        ),
        migrations.DeleteModel(
            name='Academic',
        ),
    ]
