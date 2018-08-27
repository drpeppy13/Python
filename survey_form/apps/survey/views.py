from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'survey/index.html')

def result(request):
    return render(request, 'survey/result.html')

def process(request):
    request.session['name'] = request.POST['your_name']
    request.session['location'] = request.POST['dojo_location']
    request.session['language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')
# Create your views here.
