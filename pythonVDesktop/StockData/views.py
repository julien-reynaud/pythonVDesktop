import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def stock_data(request):
    symbol = request.GET.get('symbol', '')
    if symbol:
        response = requests.get(f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=cuuejg1r01qlidi3j1e0cuuejg1r01qlidi3j1eg")
        data = response.json()
        return JsonResponse({'price': data.get('c', 'Données non disponibles')})
    return JsonResponse({'error': 'Aucun symbole fourni'})