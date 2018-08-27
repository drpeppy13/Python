from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("I'm working")

# Create your views here.
