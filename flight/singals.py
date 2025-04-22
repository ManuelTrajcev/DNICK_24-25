from django.db.models.signals import pre_save, post_save
from .models import *
from django.dispatch import receiver

from flight.models import Flight


@receiver(pre_save, sender=Pilot)
def update_pilot_rank(sender, instance, **kwargs):

    print("pre_save called!")
