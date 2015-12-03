from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    s = "Hello!<br/><a href=\"%s\">All audios</a>" % reverse("audio:tracks")
    return HttpResponse(s)

def show_all(request):
    s = "All tracks!<br/><a href=\"%s\">Back to Index</a>" % reverse("audio:index")
    return HttpResponse(s)