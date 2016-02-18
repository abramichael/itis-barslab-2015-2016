# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0009_auto_20151203_1800'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='audio',
            unique_together=set([('title', 'artist')]),
        ),
    ]
