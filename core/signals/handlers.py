from django.db.models.signals import post_save
from django.dispatch import receiver
from .. import models



@receiver(post_save, sender=models.Channel)
def create_user_report(sender, instance, created, **kwargs):
    if created:
        models.Channel.objects.create(tgstat_link=instance)