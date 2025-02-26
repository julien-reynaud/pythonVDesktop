from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'completed')
    list_filter = ('completed', 'date')
    search_fields = ('title',)
