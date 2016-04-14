from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.shortcuts import render
import time

from audio.forms import AudioForm, AudioDataForm
from audio.models import Audio, Artist, genres


def main(request):
    if request.user.is_authenticated():
        if request.COOKIES.has_key("page"):
            return redirect(reverse(request.COOKIES["page"]))
        else:
            return redirect(reverse("audio:index"))
    else:
        return redirect(reverse("login"))


def login(request):
    # authenticated user does not need to log in
    if request.user.is_authenticated():
        return redirect(reverse("audio:index"))

    if request.method == "GET":
        context = {}
        if "next" in request.GET:
            context["next"] = "?next=" + request.GET["next"]
        return render(request, "audio/login.html", context)

    elif request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user is not None:
            auth_login(request, user)
            if "next" in request.GET:
                return redirect(request.GET["next"])
            else:
                return redirect(reverse("audio:index"))
        else:
            return redirect(reverse("login"))
    else:
        return HttpResponse("405")


@login_required(login_url=reverse_lazy("login"))
def index(request):
    audios = request.user.favorites.all()

    h = render(request, "audio/index.html",
                  {"username": request.user.username,
                   "audios": audios})
    h.set_cookie(key="page", value="audio:tracks", max_age=365 * 24 * 60 * 60)
    return h


@login_required(login_url=reverse_lazy("login"))
def show_all(request):

    if request.session.has_key("visited"):
        old_time = request.session["visited"]

        if time.time() - old_time < 30:
            return HttpResponse("You have been. Here wait %s seconds" % (30 - int(time.time() - old_time)))

    s = "All tracks!<br/><a href=\"%s\">Back to Index</a><br><br>" % reverse("audio:index")

    #artist = Artist.objects.get(name="AC/DC")
    #audios = Audio.objects.filter(artist=artist)
    audios = Audio.objects.all()
    s += "".join(map(lambda x: "<li>%s</li>" % x, audios))
    request.session["visited"] = time.time()
    h = HttpResponse(s)
    h.set_cookie(key="page", value="audio:tracks", max_age=365 * 24 * 60 * 60)
    return h


def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


@login_required(login_url=reverse_lazy("login"))
def audio_page(request, audio_id):
    audio_object = Audio.objects.get(id=audio_id)
    who_favorited = audio_object.favorite.all()
    h = render(request, "audio/audio_page.html", {"audio": audio_object,
                                                     "liked": who_favorited})

    h.set_cookie(key="page", value="audio:tracks", max_age=365 * 24 * 60 * 60)
    return h

@login_required(login_url=reverse_lazy("login"))
def add_audio_old(request):
    if request.method == "GET":
        return render(request, "audio/add_audio.html", {
            "artists": Artist.objects.values("id", "name"),
            "genres": genres
        })

    elif request.method == "POST":
        a = Audio()
        a.title = request.POST["title"]
        a.artist_id = request.POST["artist"]
        a.genre = request.POST["genre"]
        a.save()
        return redirect(reverse("audio:audio_page", args=(a.id,)))
    else:
        return HttpResponse("405")


@login_required(login_url=reverse_lazy("login"))
def add_audio(request):
    if request.method == "GET":
        f = AudioForm()
        return render(request, "audio/add_audio.html", {"f": f})

    elif request.method == "POST":
        f = AudioForm(request.POST)
        if f.is_valid():
            a = f.save()
            return redirect(reverse("audio:audio_page", args=(a.id,)))
    else:
        return HttpResponse("405")


def audio_data(request, audio_id):
    if request.method == "GET":
        f = AudioDataForm()
        return render(request, "audio/audio_data_page.html", {"f": f, "audio_id": audio_id})
    elif request.method == "POST":
        return HttpResponse("405")
    else:
        return HttpResponse("405")
