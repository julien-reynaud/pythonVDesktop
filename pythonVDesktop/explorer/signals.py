import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from explorer.models import File

@receiver(post_delete, sender=File)
def delete_file_from_storage(sender, instance, **kwargs):
    # Ce signal s'assure que le fichier physique est supprimé
    if instance.file:
        try:
            if os.path.isfile(instance.file.path):
                os.remove(instance.file.path)
        except Exception as e:
            print("Erreur lors de la suppression du fichier:", e)
