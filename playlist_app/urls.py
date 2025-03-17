from django.contrib import admin
from django.urls import path, include
from tape import views as tape_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tape_views.home, name='home'),  # Use the home view from the tape app
    path('tapes/', include('tape.urls')),
    path('songs/', include('song.urls')),  # Include the song app's URLs
    path('users/', include('user.urls')),  # Include the user app's URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include the authentication URLs
]