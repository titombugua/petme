# Generated by Django 2.0 on 2018-11-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_vetinfo_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescueorganizations',
            name='descriptions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
