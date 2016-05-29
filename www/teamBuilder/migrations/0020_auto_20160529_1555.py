# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teamBuilder', '0019_restriction_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='marker',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='captain',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='project',
            name='publisher',
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_published', to=settings.AUTH_USER_MODEL),
        ),
    ]
