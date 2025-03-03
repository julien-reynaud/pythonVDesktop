# terminal/urls.py
from django.urls import path
from . import views

app_name = 'terminal'  # Définir un namespace pour cette app

urlpatterns = [
    path("", views.affiche_terminal, name="Terminal"),
    path("execute/", views.execute_command, name="Execute"),
]
