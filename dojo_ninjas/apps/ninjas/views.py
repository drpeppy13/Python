from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("I'm working right now")

# Create your views here.
