from audio.models import Audio, Artist, Duet
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    s = "Hello!<br/><a href=\"%s\">All audios</a>" % reverse("audio:tracks")
    return HttpResponse(s)

def show_all(request):
    s = "All tracks!<br/><a href=\"%s\">Back to Index</a><br><br>" % reverse("audio:index")

    #audios = Audio.objects.all()
    #audios = Audio.objects.order_by("-anon_likes")
    #audios = Audio.objects.filter(artist="AC/DC")
    #audios = Audio.objects.filter(anon_likes__gte=6000)
    #audios = Audio.objects.filter(title__icontains="s")

    #artist = Artist.objects.get(name="AC/DC")
    #audios = Audio.objects.filter(artist=artist)

    #audios = Audio.objects.filter(artist__name="AC/DC").order_by('title')

    #artist = Artist.objects.get(name="AC/DC")
    #audios = artist.audios.all()

    #s += "".join(map(lambda x: "<li>%s</li>" % x, [audio.title for audio in audios]))

    #s += "".join(map(lambda x: "<li>%s</li>" % x, audios))

    audio = Duet.objects.get(title="Cool song")
    artist = Artist.objects.get(name="Red Hot Chili Peppers")

    audios = artist.audios_from_duet.all()

    s += "".join(map(lambda x: "<li>%s</li>" % x, audios))


    



    return HttpResponse(s)