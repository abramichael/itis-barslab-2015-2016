# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import audio.models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0015_artist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(null=True, upload_to=audio.models.get_artist_image_path),
        ),
    ]
