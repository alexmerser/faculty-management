# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=30)),
                ('submitted', models.DateTimeField()),
                ('presented', models.DateTimeField()),
                ('review', models.TextField()),
                ('subject', models.ForeignKey(to='subjects.Subject')),
            ],
            options={
                'verbose_name_plural': 'Researches',
            },
        ),
    ]
