from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # Titre de la tâche
    description = models.TextField(blank=True, null=True)  # Description optionnelle
    date = models.DateField()  # Date de la tâche
    time = models.TimeField()  # Heure de la tâche
    completed = models.BooleanField(default=False)  # Statut complété ou non

    def __str__(self):
        return self.title
