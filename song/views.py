from django.shortcuts import render, get_object_or_404, redirect
from .models import Song
from .forms import SongForm
import requests
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

def get_access_token():
    # Encode client ID and client secret
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    # Get access token
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {b64_auth_str}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(token_url, headers=headers, data=data)
    response_data = response.json()
    access_token = response_data.get("access_token")

    if not access_token:
        raise Exception("Could not get access token")

    return access_token

def get_album_art_url(track, artist):
    access_token = get_access_token()

    # Create search query
    query = f"track:{track} artist:{artist}"
    search_url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "q": query,
        "type": "track",
        "limit": 1
    }

    response = requests.get(search_url, headers=headers, params=params)
    search_results = response.json()

    # Check if any tracks were found
    if not search_results['tracks']['items']:
        raise Exception("No tracks found")

    # Extract album art URL directly from search results
    album_art_url = search_results['tracks']['items'][0]['album']['images'][0]['url']
    return album_art_url

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'song/song_detail.html', {'song': song})

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'song/song_form.html', {'form': form})

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
    return render(request, 'song/edit_song.html', {'form': form, 'song': song})

def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'song/song_form.html', {'form': form})

def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'song/song_confirm_delete.html', {'song': song})