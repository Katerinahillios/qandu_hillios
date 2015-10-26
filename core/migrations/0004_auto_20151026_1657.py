# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151026_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
