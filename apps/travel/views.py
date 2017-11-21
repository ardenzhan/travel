# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Trip
from ..login_reg.models import User

from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'user': User.objects.get(id = request.session['user_id']),
        'other_users': User.objects.all().exclude(id = request.session['user_id']),
    }
    return render(request, 'travel/index.html', context)

def add(request):
    return render(request, 'travel/add.html')

def show(request, trip_id):
    context = {
        'trip': Trip.objects.get(id = trip_id)
    }
    return render(request, 'travel/show.html', context)

def join(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    traveler = User.objects.get(id=request.session['user_id'])
    traveler.trips.add(trip)
    traveler.save()

    return redirect('/travels')

def create(request):
    result = Trip.objects.validate_trip(request.POST, request.session['user_id'])

    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/travels/add')

    return redirect('/travels')