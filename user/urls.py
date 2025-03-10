from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns here
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]