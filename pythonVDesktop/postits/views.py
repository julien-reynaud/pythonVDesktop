from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Affichage du postit
def affichage_postit(request):
    return render(request, 'postits/templates/postits.html')

# Ajout d'un postit
@csrf_exempt
def quick_note(request):
    if request.method == 'POST':
        # Here you can add any logic to save the post-it note if needed
            return JsonResponse({'success': True})
    return render(request, 'postits/templates/postits.html')