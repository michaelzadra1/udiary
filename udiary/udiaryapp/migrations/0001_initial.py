# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 15:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('FName', models.CharField(max_length=20)),
                ('LName', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('DOB', models.DateTimeField(verbose_name='date of birth')),
                ('Gender', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.TextField()),
                ('texttags', models.TextField()),
                ('keywords', models.TextField()),
                ('people', models.TextField()),
                ('places', models.TextField()),
                ('personality', models.TextField()),
                ('emotion', models.TextField()),
                ('personas', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(verbose_name='date added')),
                ('Text', models.TextField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='analysis',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udiaryapp.Entry'),
        ),
    ]
