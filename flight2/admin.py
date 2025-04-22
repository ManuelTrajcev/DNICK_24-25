from django.contrib import admin

from flight.models import Flight
from flight2.models import *
# Register your models here.

class AirlinePilotInline(admin.TabularInline):
    model = AirlinePilot
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)

    def has_change(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
class PilotAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
    list_filter = ("name", "surname")

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

        return False


class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name", "year_founded", "outside_Europe")
    inlines = (AirlinePilotInline,)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

        return False


admin.site.register(Flight_2, FlightAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon)
admin.site.register(AirlinePilot)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(FlightReport)
admin.site.register(FlightLog)
