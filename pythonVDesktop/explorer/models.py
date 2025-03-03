from django.db import models
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Drive(models.Model):
    DRIVE_TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('common', 'Common'),
        ('admin', 'Admin'),
    )
    drive_type = models.CharField(max_length=20, choices=DRIVE_TYPE_CHOICES)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='drives',
        help_text="Obligatoire pour un drive personnel."
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.drive_type == 'personal' and self.owner:
            return f"{self.owner.username}'s Drive: {self.name}"
        return f"{self.get_drive_type_display()} Drive: {self.name}"

class Directory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='subdirectories'
    )
    drive = models.ForeignKey(
        Drive,
        on_delete=models.CASCADE,
        related_name='directories'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def get_full_path(self):
        parts = []
        directory = self
        while directory:
            parts.insert(0, directory.name)
            directory = directory.parent
        return os.path.join(*parts)

    def get_url_path(self):
        return str(self.id)

    def get_ancestors_list(self):
        ancestors = []
        current = self
        while current:
            ancestors.insert(0, current)
            current = current.parent
        return ancestors

class File(models.Model):
    name = models.CharField(max_length=255)
    directory = models.ForeignKey(
        Directory,
        on_delete=models.CASCADE,
        related_name='files'
    )
    file = models.FileField(upload_to='explorer_files/')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='files',
        null=True,
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def extension(self):
        return os.path.splitext(self.file.name)[1].lower()
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Supprime le fichier du système de fichiers
        if self.file:
            try:
                if os.path.isfile(self.file.path):
                    os.remove(self.file.path)
            except Exception as e:
                print("Erreur lors de la suppression du fichier:", e)
        super().delete(*args, **kwargs)
