from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tape
from song.models import Song
from .forms import TapeForm, AddSongForm, EditSongForm, DeleteSongsForm

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
    tape = get_object_or_404(Tape, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AddSongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.tape = tape
            song.user = request.user
            song.save()
            return redirect('tape_detail', pk=tape.pk)
    else:
        form = AddSongForm()
    return render(request, 'tape/add_song_to_tape.html', {'form': form, 'tape': tape})

@login_required
def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EditSongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('tape_detail', pk=song.tape.pk)
    else:
        form = EditSongForm(instance=song)
    return render(request, 'tape/edit_song.html', {'form': form, 'song': song})

@login_required
def delete_songs_from_tape(request, pk):
    tape = get_object_or_404(Tape, pk=pk, user=request.user)
    songs = tape.songs.filter(user=request.user)
    if request.method == 'POST':
        form = DeleteSongsForm(request.POST, queryset=songs)
        if form.is_valid():
            form.save()
            return redirect('tape_detail', pk=tape.pk)
    else:
        form = DeleteSongsForm(queryset=songs)
    return render(request, 'tape/delete_songs_from_tape.html', {'form': form, 'tape': tape})