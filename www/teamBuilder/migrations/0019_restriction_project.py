# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamBuilder', '0018_auto_20160527_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='restriction',
            name='project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teamBuilder.Project'),
        ),
    ]
