# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='staff',
            field=models.ForeignKey(to='users.Staff', default=1),
            preserve_default=False,
        ),
    ]
