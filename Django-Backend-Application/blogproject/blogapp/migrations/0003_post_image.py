# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'media/images'),
        ),
    ]
