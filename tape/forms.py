from django import forms
from .models import Tape

class TapeForm(forms.ModelForm):
    class Meta:
        model = Tape
        fields = ['title', 'description']