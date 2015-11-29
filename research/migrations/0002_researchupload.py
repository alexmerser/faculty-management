# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151123_1448'),
        ('subjects', '0002_subject_staff'),
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchUpload',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('subject', models.ForeignKey(to='subjects.Subject')),
                ('user', models.ForeignKey(to='users.Student')),
            ],
        ),
    ]
