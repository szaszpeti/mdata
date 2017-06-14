# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meditator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('country', models.CharField(max_length=120)),
                ('born', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('phone', models.CharField(max_length=60)),
                ('profession', models.CharField(max_length=60)),
                ('course', models.CharField(max_length=60)),
                ('course_date', models.DateField()),
                ('teacher', models.CharField(max_length=60)),
                ('remarks', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
