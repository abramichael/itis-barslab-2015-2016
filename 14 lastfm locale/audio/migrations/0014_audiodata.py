# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0013_audio_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('bitrate', models.PositiveSmallIntegerField(null=True)),
                ('duration', models.IntegerField()),
                ('phone_of_author', models.CharField(max_length=20, blank=True)),
                ('description', models.TextField(blank=True)),
                ('audio', models.ForeignKey(to='audio.Audio')),
            ],
        ),
    ]
