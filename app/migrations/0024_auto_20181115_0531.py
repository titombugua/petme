# Generated by Django 2.0 on 2018-11-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20181114_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petsinfo',
            name='image',
            field=models.CharField(max_length=25000, null=True),
        ),
    ]
