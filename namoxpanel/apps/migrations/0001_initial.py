# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-02 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=240, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('version', models.CharField(blank=True, default='1.0', max_length=15, null=True, unique=True)),
                ('stack', models.BooleanField(default=False)),
                ('db_engine', models.CharField(blank=True, choices=[('postgres', 'PostgreSQL'), ('mysql', 'MySql'), ('mariadb', 'MariaDB'), ('sqlite', 'SQLite')], default='postgres', max_length=200, null=True)),
                ('db_name', models.CharField(blank=True, max_length=180, null=True)),
                ('db_dump', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('git_repo', models.TextField(blank=True, null=True)),
                ('dockerized', models.BooleanField(default=False)),
                ('admin_panel', models.BooleanField(default=False)),
                ('technology', models.CharField(blank=True, choices=[('rest', 'REST'), ('soap', 'SOAP'), ('websocket', 'WebSocket'), ('e-commerce', 'E-Commerce'), ('e-commerce-api', 'E-commerce API'), ('blog', 'Blog'), ('blog-api', 'Blog API'), ('personal-page', 'Personal Page')], default='rest', max_length=200, null=True)),
                ('output', models.CharField(blank=True, choices=[('json', 'JSON'), ('yalm', 'YALM')], default='json', max_length=200, null=True)),
                ('request_log', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'app',
                'verbose_name_plural': 'apps',
            },
        ),
    ]
