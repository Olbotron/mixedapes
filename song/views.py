from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Song  # Import the Song model
from .forms import SongForm, EditSongForm  # Import the SongForm
from tape.models import Tape  # Import the Tape model from the correct module
from .utils import get_album_art_url  # Import the get_album_art_url function

@login_required
def song_list(request):
    songs = Song.objects.filter(user=request.user)  # Filter songs by the current user
    return render(request, 'song/song_list.html', {'songs': songs})

@login_required
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk, user=request.user)  # Ensure the song belongs to the current user
    return render(request, 'song/song_detail.html', {'song': song})

@login_required
def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user  # Set the user field
            try:
                album_art_url = get_album_art_url(song.title, song.artist)
                song.album_art_url = album_art_url
            except Exception as e:
                print(f"Error fetching album art URL: {e}")
            song.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'song/song_form.html', {'form': form})

@login_required
def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if song.tape.user != request.user:
        return redirect('tape_detail', pk=song.tape.pk)  # Redirect if the user is not the owner
    if request.method == 'POST':
        form = EditSongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save(commit=False)
            try:
                song.album_art_url = get_album_art_url(song.title, song.artist)
            except Exception as e:
                print(f"Error fetching album art URL: {e}")
                song.album_art_url = "https://example.com/default_album_art.jpg"  # Set a default album art URL
            song.save()
            return redirect('tape_detail', pk=song.tape.pk)
    else:
        form = EditSongForm(instance=song)
    return render(request, 'song/edit_song.html', {'form': form, 'song': song})

@login_required
def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk, user=request.user)  # Ensure the song belongs to the current user
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save(commit=False)
            try:
                album_art_url = get_album_art_url(song.title, song.artist)
                song.album_art_url = album_art_url
            except Exception as e:
                print(f"Error fetching album art URL: {e}")
            song.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'song/song_form.html', {'form': form, 'song': song})

@login_required
def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk, user=request.user)  # Ensure the song belongs to the current user
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'song/song_confirm_delete.html', {'song': song})