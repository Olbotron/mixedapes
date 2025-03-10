from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True, null=True)
    album_art_url = models.URLField(max_length=200, blank=True, null=True)
    tape = models.ForeignKey('tape.Tape', on_delete=models.CASCADE, related_name='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title