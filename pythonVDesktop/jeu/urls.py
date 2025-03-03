from django.urls import path
from . import views

urlpatterns = [
    path('', views.affiche_jeu, name='affiche_jeu'),
    path('get-scores/', views.get_scores, name='get_scores'),
    path('update-score/', views.update_score, name='update_score'),
]
