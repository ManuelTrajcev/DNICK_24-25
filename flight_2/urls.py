"""
URL configuration for flight_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from flight2 import views as FlightAppViews

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("flight/", FlightAppViews.index, name="flight_index"),
                  path("add-flight/", FlightAppViews.add_flight_view, name="add_flight_view"),
                  path("contact/", FlightAppViews.contact, name="contact"),
                  path("details/<flight_id>", FlightAppViews.details, name="details"),
                  path("edit-flight/<flight_id>", FlightAppViews.edit_flight, name="edit_flight"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
