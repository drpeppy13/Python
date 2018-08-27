from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1

	word = get_random_string(length=14)
	context = {'word': word}

	return render(request, "rand_word/index.html", context)

def reset(request):
	if 'counter' in request.session:
		del request.session['counter']

	return redirect('/')
# Create your views here.
