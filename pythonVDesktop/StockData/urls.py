from django.urls import path
from .views import get_stock_data

urlpatterns = [
    path('<str:symbol>/', get_stock_data, name='get_stock_data'),
]