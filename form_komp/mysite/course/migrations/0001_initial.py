# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=6)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('about', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=20)),
                ('tr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.TrainingPrograms')),
            ],
        ),
        migrations.CreateModel(
            name='PredCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr_cours', to='course.Course')),
                ('prcours', models.ManyToManyField(related_name='pr_predcours', to='course.Course')),
            ],
        ),
        migrations.AddField(
            model_name='competence',
            name='course',
            field=models.ManyToManyField(to='course.Course'),
        ),
        migrations.AddField(
            model_name='competence',
            name='tr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.TrainingPrograms'),
        ),
    ]