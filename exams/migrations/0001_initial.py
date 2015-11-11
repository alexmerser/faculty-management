# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('subjects', '0002_auto_20151111_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hours', models.PositiveIntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=2, choices=[(b'A+', b'A+'), (b'A', b'A'), (b'B+', b'B+'), (b'B', b'B'), (b'C+', b'C+'), (b'C', b'C'), (b'D+', b'D+'), (b'D', b'D'), (b'F', b'F')])),
                ('exam', models.ForeignKey(to='exams.Exam')),
                ('student', models.ForeignKey(to='users.Student')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_type',
            field=models.ForeignKey(to='exams.ExamType'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(to='subjects.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together=set([('exam_type', 'subject', 'date')]),
        ),
    ]
