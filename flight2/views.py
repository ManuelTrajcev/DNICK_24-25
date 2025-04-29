from django.http import HttpResponse
from django.shortcuts import render
import os
import django

from flight2.models import Flight_2

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_2.settings')
django.setup()


# Create your views here.

def index(request):
    flights = Flight_2.objects.all()
    context = {'flights': flights, 'app_name': 'FlightApp'}
    return render(request, 'index.html', context)


def details(request, flight_id):
    flight = Flight_2.objects.filter(pk=flight_id).first()
    context = {'flight': flight}
    return render(request, 'details.html', context)
