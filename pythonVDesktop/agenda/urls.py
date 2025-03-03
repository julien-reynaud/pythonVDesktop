from django.urls import path
from .views import task_and_calendar_view, add_task, edit_task, delete_task

urlpatterns = [
    path('', task_and_calendar_view, name='task_list'),  # Assure-toi que 'task_list' est bien défini ici
    path('add/', add_task, name='add_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
