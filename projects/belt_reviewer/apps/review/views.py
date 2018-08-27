from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import*

def index(request):
    if "id" not in request.session:
        request.session['id']= 0

    return render(request, 'review/index.html')

def register(request):
    if request.method == "POST":
        new_user = User.objects.validate_registration(request.POST)
        if "errors" in new_user:
            for error in new_user['errors']:
                messages.error(request, error)
            return redirect('/')
        if "registered_user" in new_user:
            messages.success(request, new_user['registered_user'].email_address+"'s account has been created!")        
        return redirect('/')

def login(request):
    if request.method == "POST":
        existing_user = User.objects.validate_login(request.POST)
        if "error" in existing_user:
            messages.error(request, existing_user["error"])
            return redirect('/')
        if "logged_in_user" in existing_user:
            request.session["id"] = existing_user["logged_in_user"].id
            messages.success(request, "Welcome, "+existing_user["loggeind_in_user"].alias+"!")
            return redirect('/books')
 
def create_new_book(request):
    context ={
        "authors" : Author.objects.all()
    }
    return render(request, 'review/create.html', context)
    

def add_book(request):
    if request.method == "POST":
        added_book = Book.objects.validate_book(request.POST)
        if "errors" in added_book:
            for error in added_book["errors"]:
                messages.error(request, error)
            return redirect('/add')
        if "book" in added_book:
            print added_book["book"].id
            return redirect('/books/'+str(added_book['book'].id))
def display_landing(request):
    context = {
        "books": Book.objects.order_by("created_at"),
        "reviews": Review.objects.order_by("-created_at")[:3]
    }
    return render(request, "belt/landing_page.html", context)

def display_book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "author": Author.objects.get(book_author_id=book_id),
        "book_reviews": Review.objects.filter(book_id=book_id),
        "user": User.objects.filter(user_review_book_id=book_id)
    }
    return render(request, 'review/book.html', context)

def add_review(request, book_id):
    if request.method == "POST":
        added_review = Review.objects.validate_review(request.POST)
        if "errors" in added_review:
            for error in added_review["errors"]:
                messages.error(request, error)
            return redirect('/books/'+str(book_id))
        if "review" in added_review:
            return redirect('/books/'+str(book_id))

def display_user(request, user_id):
    context = {
        "user": User.objects.get(id=user_id),
        "books": Book.objects.filter(book_review_user_id=user_id)
    }
    return render(request, 'review/user.html', context )
# def index(request):
#     return render(request, 'review/index.html')

# def index(request):
#     return render(request, 'review/index.html')

# def index(request):
#     return render(request, 'review/index.html')

# Create your views here