import requests
from django.shortcuts import render

def meteo_view(request):
    API_KEY = "a2381246b7ced2927bfdbe6857fcb84b"  # Remplace par ta clé API OpenWeather

    # Récupérer la ville saisie dans le formulaire (sinon mettre une valeur par défaut)
    city = request.GET.get("city", "Paris")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr"

    response = requests.get(url)
    data = response.json()

    weather = None
    error = None

    if response.status_code == 200:
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
        }
    else:
        error = "❌ Ville introuvable. Veuillez essayer une autre ville."

    return render(request, "meteo/meteo.html", {"weather": weather, "error": error})
