from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page to list rooms
    path('<str:room_name>/', views.room, name='room'),  # Specific room page
]
