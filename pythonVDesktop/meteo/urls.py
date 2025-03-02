from django.urls import path
from .views import meteo_view

urlpatterns = [
    path("", meteo_view, name="meteo"),
]
