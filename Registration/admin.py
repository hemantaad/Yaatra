from django.contrib import admin
from .models import Buses, Driver


class BusesAdmin(admin.ModelAdmin):
    list_display = ('yatayat', 'source', 'destination', 'date', 'time')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'number', 'busnumber', 'fare')


admin.site.register(Buses, BusesAdmin)

admin.site.register(Driver, DriverAdmin)
