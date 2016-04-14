# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0005_audio_anon_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='genre',
            field=models.CharField(max_length=4, null=True, choices=[(b'rock', b'Rock'), (b'hm', b'Heavy Metal'), (b'pop', b'Pop music'), (b'pth', b'Patriotic Trance House')]),
        ),
    ]
