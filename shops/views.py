from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.contrib.gis.geos.point import Point

longitude = 37.016033
latitude = -1.107004
user_location = Point(longitude, latitude, srid=4326)
# Create your views here.


class ShopList(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance(
        'location', user_location)
    ).order_by('distance')[0:20]
    template_name = 'shops/index.html'
