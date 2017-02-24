# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.TextField(verbose_name='Card ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
        ),
    ]
