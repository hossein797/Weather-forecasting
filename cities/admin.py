from django.contrib import admin
# Register your models here.
from .models import Location, Weather

admin.site.register(Location)
admin.site.register(Weather)
