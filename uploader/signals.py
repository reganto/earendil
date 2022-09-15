from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from .models import Video
from .tasks import convert


@receiver(post_save, sender=Video)
def convert_videos(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: convert.delay(instance.id))
