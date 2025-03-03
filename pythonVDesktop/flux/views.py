import requests
from django.shortcuts import render

def flux_view(request):
    API_KEY = "a2a69ff3b0324c7c8bb8036ab1c7937d"  # Remplace par ta clé API de NewsAPI
    category = request.GET.get("category", "general")  # Récupère la catégorie ou "general" par défaut
    language = request.GET.get("language", "en")  # Récupère la langue ou "en" par défaut

    url = f"https://newsapi.org/v2/top-headlines?category={category}&language={language}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        articles = data["articles"]
    else:
        articles = []

    return render(request, "flux/flux.html", {"articles": articles, "category": category, "language": language})
