# Generated by Django 2.0 on 2018-11-14 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownerinfo',
            name='petInfo',
        ),
        migrations.AddField(
            model_name='ownerinfo',
            name='pet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.pet'),
            preserve_default=False,
        ),
    ]
