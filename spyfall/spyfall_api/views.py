from django.shortcuts import render
from .models import Locations
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import LocationsSerializer


# Create your views here.

# @api_view(['GET'])
def locationList(request):
    if request.method == 'GET':
        locations = Locations.objects.all()
        location_serializer = LocationsSerializer(locations, many=True)
        return JsonResponse(locations, safe=False)
