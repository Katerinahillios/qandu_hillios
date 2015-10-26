# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151026_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b''), (1, b'Mr'), (2, b'Ms'), (3, b'Mrs'), (4, b'Dr')]),
        ),
    ]
