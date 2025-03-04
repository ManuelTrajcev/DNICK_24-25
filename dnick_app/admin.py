from django.contrib import admin
from .models import *
# Register your models here.


#inline models
class AirlinePilotInline(admin.TabularInline):
    model = AirlinePilot
    extra = 2   #definira kolku prazni polinja da se prikazat inicijalno

# Klasa za prikaz vo admin panel

class PilotAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'total_hours')      #koi polinja da se prikazuvaat, no str ostanuva vo choices kaj drugite modeli

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_founded')
    inlines = [AirlinePilotInline]

class FlightAdmin(admin.ModelAdmin):
    exclude = ["created_by",]
    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if obj.created_by == request.user:
                return True
            else:
                return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)


admin.site.register(Pilot, PilotAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(AirlinePilot)
admin.site.register(Balloon)
admin.site.register(Flight, FlightAdmin)