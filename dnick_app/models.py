from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Pilot(models.Model):
    RANK = [
        ("J", "Junior"),
        ("I", "Intermediate"),
        ("S", "Senior")
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    total_hours = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.CharField(max_length=1, choices=RANK)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Balloon(models.Model):
    TYPE = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE)
    manufacturer = models.CharField(max_length=100)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.type}"

class Airline(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    out_of_europe = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.airline} {self.pilot}"

class Flight(models.Model):
    code = models.CharField(max_length=10)
    takes_off_airport = models.CharField(max_length=100)
    landing_airport = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    airline = models.ForeignKey(AirlinePilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.takes_off_airport} {self.landing_airport}"