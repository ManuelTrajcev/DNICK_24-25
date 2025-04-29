from django.http import HttpResponse
from django.shortcuts import render
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_2.settings')
django.setup()

from flight2.models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.
#
#
# p1 = Pilot(name="Pilot1", surname="Surnam1", year_of_birth=1983, total_flight_hours=2, rank="S")
# p1.save()
# Pilot.objects.create(name="Pilot2", surname="Surname2", year_of_birth=1983, total_flight_hours=2.2, rank="S")
# Pilot.objects.all()
# print(Pilot.objects.filter(rank="S"))
# Flight_2.objects.filter(date__gt= datetime.now().date())
# print(Flight_2.objects.all())
# print(Flight_2.objects.filter(pilot__rank="S"))
# print(Flight_2.objects.filter(pilot__name="Pilot1"))
# print(Flight_2.objects.filter(pilot__name__iexact="pilot1"))
# print(Flight_2.objects.filter(pilot__name__exact="pilot1"))
# print(Pilot.objects.filter(name__contains="pilot"))
# print(Pilot.objects.all()[:2])
# print(Pilot.objects.all()[1])
# print(Pilot.objects.filter(rank="S", name="Pilot1"))   # AND
# print(Pilot.objects.filter(Q(rank="S") | Q(name="Pilot1")))   # OR  from django.db.models import Q
# print(Pilot.objects.filter(~Q(rank="S") | ~Q(name="Pilot1")))   # ~Q negacija
# print(Pilot.objects.filter(~Q(rank="S") & ~Q(name="Pilot1")))   # ~Q negacija
# print(Pilot.objects.filter(rank="J").get())
# print(Pilot.objects.filter(rank="O").get()) #Kaj get frla exception ako e empty, se koristi za PRimary key najcesto, ako ima povekj frla exception
# print(Pilot.objects.filter(rank="O").first())   #za da ne frle exceptiom
# print(Pilot.objects.all().values_list("name"))
# print(Pilot.objects.all().order_by("name"))
# print(Pilot.objects.all().order_by("-name"))
# print(Pilot.objects.filter(total_flight_hours__in=[1,2,3]))
# print(Pilot.objects.exists())
# print(Pilot.objects.filter(rank="J").exists())
# print(Pilot.objects.filter(rank="O").exists())


