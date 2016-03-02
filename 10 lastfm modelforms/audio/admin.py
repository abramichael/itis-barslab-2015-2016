from django.contrib import admin

from audio.models import Audio, Artist, Duet

admin.site.register(Audio)
admin.site.register(Artist)
admin.site.register(Duet)
