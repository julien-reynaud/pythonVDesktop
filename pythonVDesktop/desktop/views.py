from django.shortcuts import render
from .models import Shortcut

def desktop_view(request):
    shortcuts = Shortcut.objects.all()  # Récupère tous les raccourcis
    return render(request, 'desktop/desktop.html', {'shortcuts': shortcuts})
