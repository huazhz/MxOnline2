# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/image/%Y/%m', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='org/teacher/%Y/%m', verbose_name='头像'),
        ),
    ]
