# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import courses.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('course_number', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(blank=True, max_length=35)),
                ('description', models.TextField()),
                ('year', models.PositiveIntegerField(default=courses.models.get_current_year)),
                ('semester', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
