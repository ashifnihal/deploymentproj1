# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-18 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('brand', models.CharField(max_length=256)),
                ('model', models.CharField(max_length=256)),
                ('fuel', models.CharField(max_length=256)),
                ('year', models.IntegerField()),
                ('cc', models.FloatField()),
            ],
        ),
    ]
