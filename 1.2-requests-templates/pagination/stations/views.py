from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    with open(settings.BUS_STATION_CSV) as csvfile:
        data = list(csv.DictReader(csvfile))
    page_number = request.GET.get('page', 1)
    paginator = Paginator(data, 10)
    current_page = paginator.get_page(page_number)
    bus_stations =  current_page.object_list
    print(bus_stations)

    context = {
        'bus_stations': bus_stations,
        'page': current_page,
    }
    return render(request, 'stations/index.html', context)
