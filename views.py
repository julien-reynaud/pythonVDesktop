from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
import json


def virtual_os(request):
    return render(request, 'virtual_os.html')

def stock_data(request):
    symbol = request.GET.get('symbol', '')
    if symbol:
        response = requests.get(f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=cuuejg1r01qlidi3j1e0cuuejg1r01qlidi3j1eg")
        data = response.json()
        return JsonResponse({'price': data.get('c', 'Données non disponibles')})
    return JsonResponse({'error': 'Aucun symbole fourni'})


def chat_api(request):
    api_url = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}"}

    user_message = request.POST.get("message")
    payload = {"inputs": user_message}

    response = requests.post(api_url, headers=headers, json=payload)
    bot_response = response.json()[0]['generated_text']

    return JsonResponse({"response": bot_response})