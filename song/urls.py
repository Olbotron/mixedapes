from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('song/create/', views.song_create, name='song_create'),
    path('song/<int:pk>/update/', views.song_update, name='song_update'),
    path('song/<int:pk>/edit/', views.edit_song, name='edit_song'),
    path('song/<int:pk>/delete/', views.song_delete, name='song_delete'),
]