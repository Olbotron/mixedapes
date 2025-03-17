from django.urls import path
from . import views

urlpatterns = [
    path('', views.tape_list, name='tape_list'),
    path('<int:pk>/', views.tape_detail, name='tape_detail'),
    path('new/', views.tape_create, name='tape_create'),
    path('<int:pk>/edit/', views.tape_update, name='tape_update'),
    path('<int:pk>/delete/', views.tape_delete, name='tape_delete'),
    path('<int:pk>/add_song/', views.add_song_to_tape, name='add_song_to_tape'),
    path('<int:pk>/delete_songs/', views.delete_songs_from_tape, name='delete_songs_from_tape'),
    path('song/<int:pk>/edit/', views.edit_song, name='edit_song'),
]