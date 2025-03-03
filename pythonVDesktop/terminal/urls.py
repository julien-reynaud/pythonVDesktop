from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.affiche_terminal, name="Terminal"),
    path("execute/", views.execute_command, name="Execute"),
]