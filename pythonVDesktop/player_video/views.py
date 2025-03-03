from django.shortcuts import render
from googleapiclient.discovery import build
from django.conf import settings

# Fonction de recherche YouTube
def search_youtube(query):
    youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)
    
    # Effectuer la recherche de vidéos YouTube avec le terme de recherche
    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q=query,
        type="video"
    )
    response = request.execute()

    # Debug: Afficher la réponse pour vérifier la structure
    print(response)  # Affichez la réponse complète dans la console pour vérifier sa structure

    # Extraire les informations sur les vidéos
    videos = []
    for item in response["items"]:
        # Vérifier que la clé 'videoId' existe dans l'élément de réponse
        video = {}
        try:
            video["title"] = item["snippet"]["title"]
            video["description"] = item["snippet"]["description"]
            video["video_id"] = item["id"].get("videoId", None)  # Utiliser .get() pour éviter KeyError
            if video["video_id"]:  # Ajouter la vidéo seulement si un 'videoId' est trouvé
                videos.append(video)
        except KeyError as e:
            print(f"Erreur lors de l'extraction des données: {e}")
    
    return videos

# Vue pour afficher la recherche et la vidéo
def display_video(request):
    video_url = request.GET.get('video_url', '')
    video_id = None
    videos = []

    if video_url:
        # Extraire l'ID de la vidéo de l'URL fournie
        video_id = video_url.split("v=")[-1]

    # Recherche de vidéos si un terme de recherche est fourni
    search_query = request.GET.get('search', '')
    if search_query:
        videos = search_youtube(search_query)

    return render(request, 'player_video/display_video.html', {
        'video_id': video_id,
        'videos': videos,
        'search_query': search_query,
    })
