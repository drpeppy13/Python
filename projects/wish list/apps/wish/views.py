from django.shortcuts import render, redirect, HttpResponse
from models import Wish, User
import time
from django.contrib import messages
import bcrypt

def index(request): 
    if "id" not in request.session:
        request.session["id"] = None 
    return render(request, 'wish/index.html')

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
            messages.success(request, "Welcome, "+old_user['logged_in_user'].name+"!")
            return redirect('/dashboard')

def dashboard(request):
    me = request.session["id"] 
# Create your views here.
    context = { 
        "my_wish":  Wish.objects.filter(creator=me),
        "added_wish": Wish.objects.filter(wish_users=me),
        "others_wish":  Wish.objects.exclude(wish_users=me) & Wish.objects.exclude(creator=me)
    }
    return render(request, 'wish/dashboard.html', context)

def create_wish(request):
    return render(request, 'wish/add_wish.html')

def add_wish(request):
    new_item = Wish.objects.wish_validation(request.POST, request.session["id"])
    if 'error' in new_item:
        for error in new_item['error']:
            messages.error(request, error)
        return redirect('/dashboard')
    if 'new_wish' in new_item:
        messages.success(request, "Wish item created")
        return redirect('/dashboard')
    # Wish.objects.wish_add(request.session["id"], wish_id)
    # messages.success(request, "Wish item added")
    # return redirect('/dashboard')

def join_wish(request, wish_id):
    added_wish = Wish.objects.wish_add(wish_id, request.session["id"])
    if 'added_wish' in added_wish:
        messages.success(request, "Wish item added to list")
    return redirect('/dashboard')


def show_wish(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    context = {
        "wish": wish,
        "wish_users": wish.wish_users.all(),
        "wish_creators": wish.creator
    }
    return render(request, 'wish/wish.html', context)

def remove_wish(request, wish_id):
    removed_wish = Wish.objects.wish_remove(wish_id, request.session["id"])
    if 'removed_wish' in removed_wish:
        messages.success(request, "Wish item removed from list")
    return redirect('/dashboard')

def delete_wish(request, wish_id):
    deleted_wish = Wish.objects.wish_delete(wish_id, request.session["id"])
    messages.success(request, "Wish item deleted")
    return redirect('/dashboard')


def logout(request):
    request.session["id"] = None
    return redirect('/')