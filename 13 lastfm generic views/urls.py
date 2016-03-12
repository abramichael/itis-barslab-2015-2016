from django.conf.urls import url
from django.views.generic import TemplateView, ListView

from audio.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^tracks$', show_all, name='tracks'),
    url(r'^tracks$', ListView.as_view(
                    context_object_name='audios',
                    model=Audio,
                    paginate_by=5,
                    template_name='audio/all_audio.html'),
        name='tracks'),
    url(r'^tracks/(?P<audio_id>\d+)$', audio_page, name='audio_page'),
    url(r'^tracks/(?P<audio_id>\d+)/data$', audio_data_page, name='audio_data_page'),
    url(r'^tracks/new$', add_audio, name='add_audio'),
    url(r'^tracks/(?P<audio_id>\d+)/update', AudioFormView.as_view(), name='update_audio'),
    url(r'^ads/$', AdsView.as_view(), name='ads')
]
