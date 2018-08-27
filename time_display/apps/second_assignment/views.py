from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        "date": strftime("%B %W, %Y"),
        "time": strftime("%H:%M %p")
    }
    return render(request, 'second_assignment/index.html', context)

# Create your views here.
