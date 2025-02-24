from django.db import models

class Shortcut(models.Model):
    name = models.CharField(max_length=100)  # Nom du raccourci (par exemple, "Chatbot IA")
    icon = models.URLField()  # Lien vers l'icône (une URL ou un chemin relatif vers l'icône)
    command = models.CharField(max_length=255)  # Lien vers l'application ou la page à ouvrir (URL)

    def __str__(self):
        return self.name
