from django.shortcuts import render, get_object_or_404, redirect
from .models import Tape
from .forms import TapeForm, AddSongToTapeFormSet, DeleteSongsFromTapeForm
from django.contrib.auth.decorators import login_required
from song.models import Song

def home(request):
    return render(request, 'tape/home.html')

def tape_list(request):
    tapes = Tape.objects.all()
    return render(request, 'tape/tape_list.html', {'tapes': tapes})

def tape_detail(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    return render(request, 'tape/tape_detail.html', {'tape': tape})

@login_required
def tape_create(request):
    if request.method == 'POST':
        form = TapeForm(request.POST)
        if form.is_valid():
            tape = form.save(commit=False)
            tape.user = request.user  # Set the user field
            tape.save()
            return redirect('tape_list')
    else:
        form = TapeForm()
    return render(request, 'tape/tape_form.html', {'form': form})

@login_required
def tape_update(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    if tape.user != request.user:
        return redirect('tape_list')  # Redirect if the user is not the owner
    if request.method == 'POST':
        form = TapeForm(request.POST, instance=tape)
        if form.is_valid():
            form.save()
            return redirect('tape_list')
    else:
        form = TapeForm(instance=tape)
    return render(request, 'tape/tape_form.html', {'form': form})

@login_required
def tape_delete(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    if tape.user != request.user:
        return redirect('tape_list')  # Redirect if the user is not the owner
    if request.method == 'POST':
        tape.delete()
        return redirect('tape_list')
    return render(request, 'tape/tape_confirm_delete.html', {'tape': tape})

@login_required
def add_song_to_tape(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    if tape.user != request.user:
        return redirect('tape_list')  # Redirect if the user is not the owner
    if request.method == 'POST':
        formset = AddSongToTapeFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                title = form.cleaned_data.get('title')
                artist = form.cleaned_data.get('artist')
                if title and artist:
                    Song.objects.create(title=title, artist=artist, tape=tape)
            return redirect('tape_detail', pk=tape.pk)
    else:
        formset = AddSongToTapeFormSet()
    return render(request, 'tape/add_song_to_tape.html', {'formset': formset, 'tape': tape})

@login_required
def delete_songs_from_tape(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    if tape.user != request.user:
        return redirect('tape_list')  # Redirect if the user is not the owner
    if request.method == 'POST':
        form = DeleteSongsFromTapeForm(request.POST, tape=tape)
        if form.is_valid():
            songs_to_delete = form.cleaned_data['songs']
            songs_to_delete.delete()
            return redirect('tape_detail', pk=tape.pk)
    else:
        form = DeleteSongsFromTapeForm(tape=tape)
    return render(request, 'tape/delete_songs_from_tape.html', {'form': form, 'tape': tape})