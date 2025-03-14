from django.shortcuts import render, get_object_or_404, redirect
from .models import Song  # Import the Song model
from .forms import SongForm  # Import the SongForm
from tape.models import Tape  # Import the Tape model from the correct module
from .utils import get_album_art_url  # Import the get_album_art_url function

def song_list(request):
    tapes = Tape.objects.prefetch_related('songs').all()  # Use the correct related name
    return render(request, 'song/song_list.html', {'tapes': tapes})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'song/song_detail.html', {'song': song})

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            try:
                album_art_url = get_album_art_url(song.title, song.artist)
                song.album_art_url = album_art_url
            except Exception as e:
                print(f"Error fetching album art URL: {e}")
            song.save()
            return redirect('song_list')
    else:
        form = SongForm()
    tapes = Tape.objects.prefetch_related('songs').all()  # Fetch tapes and their songs
    return render(request, 'song/song_form.html', {'form': form, 'tapes': tapes})

def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
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
    tapes = Tape.objects.prefetch_related('songs').all()  # Fetch tapes and their songs
    return render(request, 'song/edit_song.html', {'form': form, 'tapes': tapes, 'song': song})

def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
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
    tapes = Tape.objects.prefetch_related('songs').all()  # Fetch tapes and their songs
    return render(request, 'song/edit_song.html', {'form': form, 'tapes': tapes, 'song': song})

def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'song/song_confirm_delete.html', {'song': song})