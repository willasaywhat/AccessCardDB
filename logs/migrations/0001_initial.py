# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('cards', '0003_auto_20170224_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_scanned', models.CharField(max_length=255, verbose_name='Card ID Scanned')),
                ('scanned_at', models.DateTimeField(auto_now_add=True, verbose_name='Time Scanned')),
                ('card_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.Card')),
                ('member_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
        ),
    ]
