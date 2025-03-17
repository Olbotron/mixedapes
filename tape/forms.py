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
        fields = ['title', 'artist', 'album', 'album_art_url']

class EditSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'album_art_url']

class DeleteSongsForm(forms.Form):
    songs = forms.ModelMultipleChoiceField(
        queryset=Song.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)
        super().__init__(*args, **kwargs)
        if queryset is not None:
            self.fields['songs'].queryset = queryset

    def save(self):
        songs_to_delete = self.cleaned_data['songs']
        songs_to_delete.delete()

class AddSongToTapeForm(forms.Form):
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=100)

AddSongToTapeFormSet = formset_factory(AddSongToTapeForm, extra=3)  # Adjust 'extra' to the number of forms you want to display

class DeleteSongsFromTapeForm(forms.Form):
    songs = forms.ModelMultipleChoiceField(
        queryset=Song.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        tape = kwargs.pop('tape', None)
        super().__init__(*args, **kwargs)
        if tape:
            self.fields['songs'].queryset = tape.songs.all()