from django.urls import path
from . import views

urlpatterns = [
    path('', views.tape_list, name='tape_list'),
    path('<int:pk>/', views.tape_detail, name='tape_detail'),
    path('new/', views.tape_create, name='tape_create'),
    path('<int:pk>/edit/', views.tape_update, name='tape_update'),
    path('<int:pk>/delete/', views.tape_delete, name='tape_delete'),
]