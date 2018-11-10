# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-10 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doorNo', models.CharField(max_length=50, null=True)),
                ('street', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(choices=[('Abu Dhabi', 'Abu Dhabi'), ('Ajman', 'Ajman'), ('Sharjah', 'Sharjah'), ('Dubai', 'Dubai'), ('Fujairah', 'Fujairah'), ('Ras Al Khaimah', 'Ras Al Khaimah'), ('Umm Al Quwain', 'Umm al Quwain')], max_length=30)),
                ('emirate', models.CharField(choices=[('Abu Dhabi', 'Abu Dhabi'), ('Ajman', 'Ajman'), ('Sharjah', 'Sharjah'), ('Dubai', 'Dubai'), ('Fujairah', 'Fujairah'), ('Ras Al Khaimah', 'Ras Al Khaimah'), ('Umm Al Quwain', 'Umm al Quwain')], max_length=30)),
                ('zipCode', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='careTakerInfo',
            fields=[
                ('ctId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('affiliation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('faqId', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('answers', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='jobExperience',
            fields=[
                ('jeId', models.AutoField(primary_key=True, serialize=False)),
                ('noOfYears', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='jobsList',
            fields=[
                ('jId', models.AutoField(primary_key=True, serialize=False)),
                ('jobName', models.CharField(max_length=30)),
                ('jobCategories', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('workingHours', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lostAndFound',
            fields=[
                ('lfId', models.AutoField(primary_key=True, serialize=False)),
                ('reportingActivity', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('emirate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ownerInfo',
            fields=[
                ('oId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='petFriendlyVenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
                ('landmark', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('emirate', models.CharField(max_length=30)),
                ('zipCode', models.IntegerField()),
                ('latitude', models.IntegerField()),
                ('logitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='petInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='petLostFoundInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfPet', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('weight', models.CharField(choices=[('w1', '0-25 lbs'), ('w2', '25-50 lbs'), ('w3', '50-100 lbs'), ('w4', '100+ lbs')], max_length=30)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('shelter', models.CharField(max_length=30)),
                ('additionalInfo', models.CharField(max_length=30, null=True)),
                ('additionalData', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='petMeServices',
            fields=[
                ('sId', models.AutoField(primary_key=True, serialize=False)),
                ('pets', models.CharField(max_length=30)),
                ('services', models.CharField(max_length=30)),
                ('created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='petServices',
            fields=[
                ('psId', models.AutoField(primary_key=True, serialize=False)),
                ('serviceName', models.CharField(max_length=30)),
                ('seviceCost', models.IntegerField()),
                ('serviceDuration', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PetsInfo',
            fields=[
                ('petId', models.AutoField(primary_key=True, serialize=False)),
                ('petName', models.CharField(max_length=30)),
                ('petBreed', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='/uploads')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=30)),
                ('birthday', models.DateField()),
                ('weight', models.CharField(choices=[('w1', '0-25 lbs'), ('w2', '25-50 lbs'), ('w3', '50-100 lbs'), ('w4', '100+ lbs')], max_length=30)),
                ('favoriteThings', models.CharField(max_length=30)),
                ('food', models.CharField(max_length=500)),
                ('anythingElse', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PetsPersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('identification', models.CharField(max_length=100)),
                ('petId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PetsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='petWas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifically', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='rescueOrganizations',
            fields=[
                ('roId', models.AutoField(primary_key=True, serialize=False)),
                ('organizationName', models.CharField(max_length=30)),
                ('webSite', models.CharField(max_length=30)),
                ('facebookLink', models.CharField(max_length=30)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
            ],
        ),
        migrations.CreateModel(
            name='VetInfo',
            fields=[
                ('vId', models.AutoField(primary_key=True, serialize=False)),
                ('certification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Certification')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='petservices',
            name='petId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PetsInfo'),
        ),
        migrations.AddField(
            model_name='petlostfoundinfo',
            name='petWas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.petWas'),
        ),
        migrations.AddField(
            model_name='petinfo',
            name='petId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PetsInfo'),
        ),
        migrations.AddField(
            model_name='petinfo',
            name='petPersonalInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PetsPersonalInfo'),
        ),
        migrations.AddField(
            model_name='ownerinfo',
            name='petInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.petInfo'),
        ),
        migrations.AddField(
            model_name='ownerinfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lostandfound',
            name='oId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ownerInfo'),
        ),
        migrations.AddField(
            model_name='lostandfound',
            name='petInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.petInfo'),
        ),
        migrations.AddField(
            model_name='jobslist',
            name='petId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PetsInfo'),
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='jId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobsList'),
        ),
        migrations.AddField(
            model_name='caretakerinfo',
            name='jobExperience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobExperience'),
        ),
        migrations.AddField(
            model_name='caretakerinfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
