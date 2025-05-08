from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from main.models import Car


def cars_list_view(request):
    """Отображает список всех автомобилей"""
    template_name = 'main/list.html'
    cars = Car.objects.all()
    return render(request, template_name, {'cars': cars})


def car_details_view(request, car_id):
    """Отображает детали автомобиля по ID"""
    car = get_object_or_404(Car, pk=car_id)
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})


def sales_by_car(request, car_id):
    """Отображает продажи конкретного автомобиля"""
    car = get_object_or_404(Car, pk=car_id)
    template_name = 'main/sales.html'
    return render(request, template_name, {'sales': car.sales.all()})
