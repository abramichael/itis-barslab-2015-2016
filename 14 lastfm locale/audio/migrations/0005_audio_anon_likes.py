# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_auto_20151203_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='anon_likes',
            field=models.IntegerField(default=0),
        ),
    ]
