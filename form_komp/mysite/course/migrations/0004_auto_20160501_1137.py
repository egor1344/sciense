# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20160501_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competence',
            old_name='cours',
            new_name='course',
        ),
    ]