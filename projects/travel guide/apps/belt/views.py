from django.shortcuts import render, redirect, HttpResponse
from .models import *
import time
from django.contrib import messages
import bcrypt

def index(request):
    if "id" not in request.session:
        request.session["id"] = None 
    return render(request, 'belt/index.html')

def register(request):
    if request.method == "POST":
        new_user = User.objects.register_validation(request.POST)
        if 'errors' in new_user:
            for error in new_user['errors']:
                messages.error(request, error)
            return redirect('/')
        if 'registered_user' in new_user:
            messages.success(request, 'The username has been created!')
            return redirect('/')

def login(request):
    if request.method =="POST":
        old_user = User.objects.login_validation(request.POST)
        if 'error' in old_user:
            for error in old_user['error']:
                messages.error(request, error)
            return redirect('/')
        if 'logged_in_user' in old_user:
            request.session["id"] = old_user['logged_in_user'].id
            messages.success(request, "Welcome, "+old_user['logged_in_user'].username)
            return redirect('/travels')

def dashboard(request):
    context = {
        "trips": Trip.objects.filter(creator_id=request.session["id"]) | Trip.objects.filter(id=request.session["id"]),
        "others_trips": Trip.objects.exclude(creator_id=request.session["id"]) & Trip.objects.exclude(id=request.session["id"])
    }
    return render(request, 'belt/dashboard.html', context)

def create_destination(request):
    return render(request, 'belt/add_trip.html')

def add_destination(request):
        new_trip = Trip.objects.trip_validation(request.POST, request.session["id"])
        if 'errors' in new_trip:
            for error in new_trip['errors']:
                messages.error(request, error)
            return redirect('/travels/add')
        if "trip" in new_trip:
            messages.success(request, "Trip added")
            return redirect('/travels')

def show_trip(request, trip_id):
    mytrip = Trip.objects.get(id=trip_id)
    context = {
        "trip": mytrip,
        "trip_users": mytrip.trip_users.all()
    }
    return render(request, 'belt/trip.html', context)

def join_trip(request, trip_id):
    join_trip = Trip.objects.trip_join(trip_id, request.session["id"])
    return redirect('/travels/destination/'+str(trip_id))

def logout(request):
    request.session["id"] = None
    return redirect('/')





# Create your views here.
