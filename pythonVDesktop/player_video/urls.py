from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.display_video, name='display_video'),
]
