# Generated by Django 2.0 on 2018-11-14 06:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20181114_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsinfo',
            name='favorite',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]