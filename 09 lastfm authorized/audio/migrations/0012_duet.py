# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0011_auto_20151203_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duet',
            fields=[
                ('audio_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='audio.Audio')),
                ('artist2', models.ForeignKey(related_name='audios_from_duet', to='audio.Artist', null=True)),
            ],
            bases=('audio.audio',),
        ),
    ]
