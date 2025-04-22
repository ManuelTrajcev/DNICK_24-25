from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from .models import *
from django.dispatch import receiver

from flight.models import Flight


# @receiver(pre_save, sender=Pilot)
# def update_pilot_pre_save(sender, instance, **kwargs):
#     import  pdb
#     pdb.set_trace()
#     print("pre_save called!")
#
# @receiver(post_save, sender=Pilot)
# def update_pilot_post_save(sender, instance, **kwargs):
#     print("post_save called!")
#
# @receiver(pre_delete, sender=Pilot)
# def update_pilot_pre_delete(sender, instance, **kwargs):
#     print("pre_delete called!")
#
# @receiver(post_delete, sender=Pilot)
# def update_pilot_post_delete(sender, instance, **kwargs):
#     print("post_delete called!")

#pre-raboti pred da se
@receiver(pre_save, sender=Pilot)  # treba pre save, bidejki ako e post_save, vekje e zacuvan objektot vo baza
def update_pilot_rank(sender, instance, **kwargs):
    if instance.total_flight_hours > 500:
        instance.rank = 'S'
    elif instance.total_flight_hours > 100:
        instance.rank = 'I'
    else:
        instance.rank = 'J'

    print("pre_save called!")


@receiver(post_save, sender=Flight_2)
def update_pilot_post_save(sender, instance, created, **kwargs):
    desc = f"Flight {instance.code} Take-off airport {instance.take_off_airport} Pilot: {instance.pilot.name} {instance.pilot.surname}"
    if created:
        FlightReport.objects.create(flight=instance, description=desc)

@receiver(pre_delete, sender=Airline)
def update_pilot_pre_delete(sender, instance, **kwargs):
    pilot_ids = AirlinePilot.objects.filter(airline=instance).values_list('pilot', flat=True)
    new_airline = Airline.objects.exclude(id=instance.id).first()
    for pilot_id in pilot_ids:
        AirlinePilot.objects.create(airline=new_airline, pilot_id=pilot_id)
    print("pre_delete called!")

@receiver(post_delete, sender=Flight_2)
def update_pilot_post_delete(sender, instance, **kwargs):
    FlightLog.objects.create(flight_code=instance.code, is_delete=True, description=f"dasdasd")
