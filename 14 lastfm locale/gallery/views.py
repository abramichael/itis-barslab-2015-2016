from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    s = "Hello!<br/><a href=\"%s\">All photos</a>" % reverse("gallery:index")
    return HttpResponse(s)

def page(request, page_number):

    s = "This is page # %s<br>" % page_number
    
    url_needed = reverse("gallery:page", args=(int(page_number)+1,))
    s += "<a href='%s'>Next page</a>" % url_needed

    return HttpResponse(s)