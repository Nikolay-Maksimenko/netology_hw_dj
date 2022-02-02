from django.contrib import admin

from measurement.models import Sensor

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'description'