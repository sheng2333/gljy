# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-30 14:20
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orginfo',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='机构详情'),
        ),
    ]
