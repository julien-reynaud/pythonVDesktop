from django.urls import path
from .views import flux_view

urlpatterns = [
    path('', flux_view, name='flux'),
]
