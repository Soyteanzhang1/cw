# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-05-05 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
    ]
