# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151023_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
