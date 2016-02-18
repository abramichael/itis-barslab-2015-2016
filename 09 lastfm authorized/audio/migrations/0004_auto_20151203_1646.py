# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_audio_album'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audio',
            options={'verbose_name_plural': '\u0410\u0443\u0434\u0438\u043e\u0437\u0430\u043f\u0438\u0441\u0438'},
        ),
        migrations.AddField(
            model_name='audio',
            name='artist',
            field=models.CharField(default=b'Unknown Artist', max_length=50),
        ),
    ]
