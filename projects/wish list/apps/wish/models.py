from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import time
import bcrypt

class UserManager(models.Manager):
    def register_validation(self, postData):
        error_messages = []
        if len(postData["name"]) < 1:
            error_messages.append("name cannot be blank") 
        elif len(postData["name"]) < 3:
            error_messages.append("name is too short")
        if len(postData["username"]) < 1:
            error_messages.append("username cannot be blank") 
        elif len(postData["username"]) < 3:
            error_messages.append("username is too short")
        if postData["birthday"] == None:
            error_messages.append("birthday cannot be blank")
        if len(postData["password"]) < 1:
            error_messages.append("password cannot be blank") 
        elif len(postData["password"]) < 8:
            error_messages.append("password is too short")
        elif postData["password"] != postData["confirm_pw"]:
            error_messages.append("passwords do not match")
        if error_messages:
            return {'errors': error_messages}
        else: 
            if User.objects.filter(username=postData["username"]).exists():
                error_messages.append("username is taken")
                return {'errors': error_messages}
            else:
                pw = postData["password"].encode()
                hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
                reg_user = User.objects.create(name=postData["name"],username=postData["username"], password=hashed, birthday=postData["birthday"])
                return {"registered_user": reg_user}

    def login_validation(self, postData):
        error_messages = []
        if len(postData["login_password"]) < 1:
            error_messages.append("password cannot be blank")
        try:
            old_user = User.objects.get(username=postData['login_username'])
            if old_user.password == bcrypt.hashpw(postData['login_password'].encode(), old_user.password.encode()):
                return {'logged_in_user': old_user}
        except User.DoesNotExist:
                error_messages.append("user does not exist")
        if error_messages:
            return {'error': error_messages}

class WishManager(models.Manager):
    def wish_validation(self, postData, id):
        item_name = postData["item"]
        error_messages = []
        if len(item_name) < 1:
            error_messages.append("Wish Item cannot be blank")
        if len(item_name) < 3:
            error_messages.append("Wish Item has to be longer than 3 characters")
        if error_messages:
            return {'error': error_messages}
        else:
            wish_user = User.objects.get(id=id)
            wish = Wish.objects.create(item_name=item_name, creator=wish_user)
            return {'new_wish': wish}

    def wish_add(self, wish_id, id):
        wish_user = User.objects.get(id=id)
        wish = Wish.objects.get(id=wish_id)
        wish.wish_users.add(wish_user)
        wish.save()
        return {'added_wish': wish}

    def wish_remove(self, wish_id, id):
        wish_user = User.objects.get(id=id)
        wish = Wish.objects.get(id=wish_id)
        wish.wish_users.remove(wish_user)
        wish.save()
        return {'removed_wish': wish}

    def wish_delete(self, wish_id, id):
        wish_creator = User.objects.get(id=id)
        wish = Wish.objects.get(id=wish_id, creator_id=id)
        wish.delete()

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=13)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.name

class Wish(models.Model):
    item_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name="wish_creator")
    wish_users = models.ManyToManyField(User, related_name="wish_user")
    objects = WishManager()