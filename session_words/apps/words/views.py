from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):
    if request.session.get('words') == None:
        request.session['words'] = []
    
    return render(request, 'words/index.html')

def process(request):
    word = request.POST['word']
    color = request.POST['color']
    if 'big_font' in request.POST:
        font = "big"
    else: 
        font = "normal"
    time = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y")

    request.session['words'].append({'word': word, 'color':color, 'font':font, 'time':time })
    request.session.modified = True
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
    

# Create your views here.
