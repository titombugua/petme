# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-11 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answers',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='petsinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='/uploads'),
        ),
    ]