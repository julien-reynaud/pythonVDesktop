from django.http import JsonResponse
from django.shortcuts import render

def affiche_jeu(request):
    # Initialisation des scores si ce n'est pas déjà fait
    if 'player_score' not in request.session:
        request.session['player_score'] = 0
    if 'computer_score' not in request.session:
        request.session['computer_score'] = 0
    return render(request, 'jeu/templates/jeu.html')

def get_scores(request):
    player_score = request.session.get('player_score', 0)
    computer_score = request.session.get('computer_score', 0)
    return JsonResponse({
        'player_score': player_score,
        'computer_score': computer_score
    })

def update_score(request):
    scorer = request.GET.get('scorer', '')

    if scorer == 'player':
        request.session['player_score'] = request.session.get('player_score', 0) + 1
    elif scorer == 'computer':
        request.session['computer_score'] = request.session.get('computer_score', 0) + 1

    return JsonResponse({
        'player_score': request.session['player_score'],
        'computer_score': request.session['computer_score']
    })
