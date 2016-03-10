# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

genres = (
        ("rock", "Rock"),
        ("hm", "Heavy Metal"),
        ("pop", "Pop music"),
        ("pth", "Patriotic Trance House"),
)


class Audio(models.Model):
    class Meta:
        db_table = "audios"
        verbose_name_plural = u'Аудиозаписи'
        unique_together = ['title', 'artist']

    title = models.CharField(max_length=50)
    artist = models.ForeignKey('Artist', related_name="audios", null=True)

    album = models.CharField(max_length=50, blank=True)
    anon_likes = models.IntegerField(default=0)
    genre = models.CharField(max_length=4, choices=genres, null=True)
    favorite = models.ManyToManyField(User, related_name="favorites")

    def __unicode__(self):
        return "%s : %s : %s - %s likes" % (self.artist, self.title, 
            self.album, self.anon_likes)

class AudioData(models.Model):
    audio = models.ForeignKey("Audio")
    year = models.PositiveSmallIntegerField(null=True)
    bitrate = models.PositiveSmallIntegerField(null=True)
    duration = models.IntegerField()
    phone_of_author = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return "%s:%s:%s" % (self.audio, self.duration, self.year)


class Artist(models.Model):
    class Meta:
        db_table = "artists"

    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.name


class Duet(Audio):
    artist2 = models.ForeignKey('Artist', related_name='audios_from_duet', null=True)