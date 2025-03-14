from django import forms
from .models import Song

# The album field is for the album cover URL. It is optional, so it can be left blank.
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'tape']