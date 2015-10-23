# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='description',
            new_name='email',
        ),
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.TextField(null=True, blank=True),
        ),
    ]
