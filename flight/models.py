from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Pilot(models.Model):
    RANK_CHOICES = [
        ("J", "Junior"),
        ("I", "Intermediate"),
        ("S", "Senior")
    ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    rank = models.CharField(max_length=1, choices=RANK_CHOICES)
    total_flights_hours = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Balloon(models.Model):
    TYPE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.manufacturer}"


class Airline(models.Model):
    name = models.CharField(max_length=50)
    year_founded = models.IntegerField()
    outside_europe = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.year_founded}"


class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.airline} {self.pilot}"

class Flight(models.Model):
    code = models.CharField(max_length=100, unique=True)
    take_off_airport = models.CharField(max_length=100)
    landing_airport = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="flight_photoss/", null=True, blank=True)
    date = models.DateField()
    airline = models.ForeignKey(AirlinePilot, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.take_off_airport} {self.landing_airport}"