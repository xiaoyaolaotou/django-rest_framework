# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-04 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20180704_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='sn',
            field=models.CharField(db_index=True, help_text='SN号', max_length=100, verbose_name='SN'),
        ),
        migrations.AlterField(
            model_name='server',
            name='uuid',
            field=models.CharField(db_index=True, help_text='UUID', max_length=100, unique=True, verbose_name='UUID'),
        ),
    ]