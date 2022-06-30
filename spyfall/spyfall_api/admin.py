from django.contrib import admin
from .models import Locations

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Locations,LocationAdmin)