from django.conf.urls import url

from audio.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tracks$', show_all, name='tracks'),
    url(r'^tracks/(?P<audio_id>\d+)$', audio_page, name='audio_page'),
    url(r'^tracks/new$', add_audio, name='add_audio')
]
