# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_auto_20151203_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='album',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
