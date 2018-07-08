# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_productcategory_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Productcondition'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Category condition'),
        ),
    ]