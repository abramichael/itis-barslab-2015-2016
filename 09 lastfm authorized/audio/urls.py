from django.conf.urls import url

from audio.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tracks$', show_all, name='tracks')
]
