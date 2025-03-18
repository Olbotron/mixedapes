from django import forms
from django.forms import formset_factory
from .models import Tape
from song.models import Song  # Import the Song model

class TapeForm(forms.ModelForm):
    class Meta:
        model = Tape
        fields = ['title', 'description']

class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        #fields = ['title', 'artist', 'album', 'album_art_url']
        fields = ['title', 'artist']

class EditSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'album_art_url']

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

class AddSongToTapeForm(forms.Form):
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)

AddSongToTapeFormSet = formset_factory(AddSongToTapeForm, extra=3)  # Adjust 'extra' to the number of forms you want to display