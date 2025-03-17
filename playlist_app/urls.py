from django.urls import path, include
from tape import views as tape_views

urlpatterns = [
    path('', tape_views.tape_list, name='tape_list'),
    path('<int:pk>/', tape_views.tape_detail, name='tape_detail'),
    path('new/', tape_views.tape_create, name='tape_create'),
    path('<int:pk>/edit/', tape_views.tape_update, name='tape_update'),
    path('<int:pk>/delete/', tape_views.tape_delete, name='tape_delete'),
    path('<int:pk>/add_song/', tape_views.add_song_to_tape, name='add_song_to_tape'),
    path('<int:pk>/delete_songs/', tape_views.delete_songs_from_tape, name='delete_songs_from_tape'),
    path('song/<int:pk>/edit/', tape_views.edit_song, name='edit_song'),
]