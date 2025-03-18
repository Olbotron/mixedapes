from django import forms
from .models import Song

# The album field is for the album cover URL. It is optional, so it can be left blank.
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']

class EditSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']

class DeleteSongsForm(forms.Form):
    songs = forms.ModelMultipleChoiceField(queryset=Song.objects.none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        tape = kwargs.pop('tape', None)
        super().__init__(*args, **kwargs)
        if tape is not None:
            self.fields['songs'].queryset = tape.songs.all()

    def save(self, commit=True):
        for song in self.cleaned_data['songs']:
            song.delete()