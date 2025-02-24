from django.urls import path
from .views import desktop_view

urlpatterns = [
    path('', desktop_view, name='desktop'),
]
