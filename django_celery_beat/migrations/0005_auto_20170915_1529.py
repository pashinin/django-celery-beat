# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-15 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0004_auto_20170221_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarschedule',
            name='event',
            field=models.CharField(max_length=24, verbose_name='event'),
        ),
    ]
