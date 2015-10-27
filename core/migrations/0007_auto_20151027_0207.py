# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151027_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='title',
            new_name='status',
        ),
    ]
