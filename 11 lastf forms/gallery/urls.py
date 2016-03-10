from django.conf.urls import url

from gallery.views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^page(?P<page_number>\d+)', page, name="page")
]