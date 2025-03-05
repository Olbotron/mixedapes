from django.shortcuts import render, get_object_or_404, redirect
from .models import Song
from .forms import SongForm

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'song/song_detail.html', {'song': song})

def song_create(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'song/song_form.html', {'form': form})

def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == "POST":
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)
    return render(request, 'song/song_form.html', {'form': form})

def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.delete()
    return redirect('song_list')