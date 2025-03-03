from django.urls import path
from . import views

app_name = 'player_video' 

urlpatterns = [
    path('video/', views.display_video, name='display_video'),
]
