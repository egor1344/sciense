# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predcourse',
            name='prcours',
            field=models.ManyToManyField(blank=True, related_name='pr_predcours', to='course.Course'),
        ),
    ]