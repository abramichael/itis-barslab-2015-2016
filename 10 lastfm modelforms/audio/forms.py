from django.forms import ModelForm
from audio.models import Audio


class AudioForm(ModelForm):
    class Meta:
        model = Audio
        fields = ["title", "artist", "genre"]
