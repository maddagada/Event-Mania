# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-12 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='chairs', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='imagesrc',
            field=models.CharField(default='/static/ember/c1.jpg', max_length=50),
        ),
    ]