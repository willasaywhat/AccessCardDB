# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_auto_20170224_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='member_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Member Name'),
        ),
    ]
