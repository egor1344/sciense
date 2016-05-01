# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20160501_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competence',
            name='course',
        ),
        migrations.AddField(
            model_name='competence',
            name='cours',
            field=models.ManyToManyField(to='course.Course'),
        ),
        migrations.AlterField(
            model_name='competence',
            name='cod',
            field=models.CharField(db_index=True, max_length=6),
        ),
    ]
