from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.affichage_postit, name="Postit"),
    path("ajout_note/", views.quick_note, name="Quick note"),
]