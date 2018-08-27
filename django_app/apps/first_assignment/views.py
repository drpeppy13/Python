from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    #url, ip of the user, browser agent, form data
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
   

def create(request):
    return redirect('/')
    
def show(request, number):
    return HttpResponse("placeholder to edit blog {}".format(number))

def edit(request, number):
    return HttpResponse("placeholder to edit blog {}".format(number)) 

def destroy(request, number):
    return redirect('/')

  

# blogs app
# / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
# /create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
# /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /. 
