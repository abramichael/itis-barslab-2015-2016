from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from audio.models import Audio

def validate_year_XX(value):
    if value < 1900:
        raise ValidationError(u'To old for our cool modern awesome uber super app!')

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ["title", "artist", "genre"]

class AudioDataForm(forms.Form):
    bitrate = forms.IntegerField()
    year = forms.IntegerField(validators=[validate_year_XX])
    duration = forms.IntegerField()
    phone_of_author = forms.CharField(
        validators=[RegexValidator(r'\+\d{,3}-\(\d{3}\)-\d{3}-\d{2}-\d{2}', "Wrong number format!")]
    )
    description = forms.CharField(widget=forms.Textarea)