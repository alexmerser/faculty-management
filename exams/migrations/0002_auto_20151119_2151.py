# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='value',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'), ('C', 'C'), ('D+', 'D+'), ('D', 'D'), ('F', 'F')], max_length=2),
        ),
    ]
