from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import os
import django

from flight2.forms import ContactForm, FlightForm
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
    print(flight)
    context = {'flight': flight}
    return render(request, 'details.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
            pass
        return redirect('flight_index')

    form = ContactForm()
    return render(request, "contacht.html", context={'form': form})


def add_flight_view(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('flight_index')

    form = FlightForm()
    return render(request, "add_fligt_form.html", context={'form': form})


def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight_2, pk=flight_id)

    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES, instance=flight)
        if form.is_valid():
            form.save()

            return redirect('flight_index')

    form = FlightForm(instance=flight)
    return render(request, "edit_flight.html", context={'form': form})
