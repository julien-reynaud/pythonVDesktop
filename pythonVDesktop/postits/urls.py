# postits/urls.py
from django.urls import path
from . import views

app_name = 'postits'  # Définir un namespace pour cette app

urlpatterns = [
    path("", views.affichage_postit, name="Postit"),
    path("ajout_note/", views.quick_note, name="Quick_note"),
]
