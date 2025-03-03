"""
URL configuration for pythonVDesktop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("terminal/", include("terminal.urls")),
    path("postits/", include("postits.urls")),
    path('Bureau/', include("Bureau.urls")),  # Route par défaut à la racine
    #path('chat-api/', views.chat_api, name='chat_api'),
    path('agenda/', include('agenda.urls')),
    path("meteo/", include("meteo.urls")),
    path('flux/', include('flux.urls')),
    path('player_video/', include('player_video.urls')),
    path('jeu/', include("jeu.urls")),
    path('get_stock_data/', include('StockData.urls')),
]
