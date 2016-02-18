# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0010_auto_20151203_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='artist',
            field=models.ForeignKey(related_name='audios', to='audio.Artist', null=True),
        ),
    ]
