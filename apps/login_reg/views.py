# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from ..travel.models import Trip
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_reg/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect(reverse("travel:index"))

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect(reverse("travel:index"))

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
