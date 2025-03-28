from django.db import models
from tape.models import Tape  # Import the Tape model
from .utils import get_album_art_url  # Import the get_album_art_url function

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True, null=True)
    album_art_url = models.URLField(blank=True, null=True)
    tape = models.ForeignKey(Tape, related_name='songs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.album_art_url:
            try:
                self.album_art_url = get_album_art_url(self.title, self.artist)
            except Exception as e:
                print(f"Error fetching album art URL: {e}")
                self.album_art_url = "https://example.com/default_album_art.jpg"  # Set a default album art URL
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title