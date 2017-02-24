# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20170224_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='status_at_scan',
            field=models.IntegerField(choices=[(1, 'Granted'), (0, 'Denied')], default=1, verbose_name='Status'),
            preserve_default=False,
        ),
    ]