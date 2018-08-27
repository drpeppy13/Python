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
                reg_user = User.objects.create(name=postData["name"], username=postData["username"], password=hashed)
                return {"registered_user": reg_user}

    def login_validation(self, postData):
        error_messages = []
        if len(postData["login_pw"]) < 1:
            error_messages.append("password cannot be blank")
        try:
            old_user = User.objects.get(username=postData['login_username'])
            if old_user.password == bcrypt.hashpw(postData['login_pw'].encode(), old_user.password.encode()):
                return {'logged_in_user': old_user}
        except User.DoesNotExist:
                error_messages.append("user does not exist")
        if error_messages:
            return {'error': error_messages}

class TripManager(models.Manager):
    def trip_validation(self, postData, id):
        current_date = time.strftime("%Y-%m-%d")
        destination = postData["destination"]
        description = postData["description"]
        start_date = postData["trip_startdate"]
        end_date = postData["trip_enddate"]
        error_messages = []
        if len(postData["destination"]) < 1:
            error_messages.append("destination cannot be blank")
        if len(postData["description"]) < 1:
            error_messages.append("description cannot be blank")
        if start_date < current_date:
            error_messages.append("start date cannot be past already")
        if end_date < start_date:
            error_messages.append("end date cannot be before start date")
        if error_messages == True:
            return {'errors': error_messages}
        else:
            trip_user = User.objects.get(id=id)
            trip = Trip.objects.create(destination=destination, description=description, trip_startdate=start_date, trip_enddate=end_date, creator=trip_user)
            return {'trip':trip}


    def trip_join(self, trip_id, id):
        trip_user = User.objects.get(id=id)
        trip = Trip.objects.get(id=trip_id)
        trip.trip_users.add(trip_user)
        trip.save()
        return {'joined_trip': trip}

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=13)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.name

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    trip_startdate = models.DateField()
    trip_enddate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name="trip_creator")
    trip_users = models.ManyToManyField(User, related_name="trip_user")
    description = models.TextField(default="")
    objects = TripManager()




        

# Create your models here.
