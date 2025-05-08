import csv
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            station = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            stations.append(station)

    paginator = Paginator(stations, 10)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'bus_stations': page_obj.object_list,
        'page': page_obj
    }
    return render(request, 'stations/index.html', context)
