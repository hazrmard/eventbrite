# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=64)),
                ('region', models.CharField(blank=True, max_length=64)),
                ('country', models.CharField(blank=True, max_length=64)),
                ('categories', models.CharField(max_length=64)),
                ('popular', models.BooleanField()),
            ],
        ),
    ]
