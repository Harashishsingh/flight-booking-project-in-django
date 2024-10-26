from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    class Meta:
        db_table = 'signup_table'
        
class table(models.Model):
    Flight_name=models.CharField(max_length=40)
    Departure=models.CharField(max_length=40)
    Destination=models.CharField(max_length=40)
    Depart=models.CharField(max_length=40)
    Time=models.CharField(max_length=40)
    class Meta:
        db_table = 'flight_table'
        
class reserve(models.Model):
    flight_id = models.ForeignKey(table,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Passenger_name=models.CharField(max_length=40)
    Email=models.CharField(max_length=40)
    Phone_number=models.CharField(max_length=40)
    Number_pass=models.CharField(max_length=40)
    Seat=models.CharField(max_length=40)
    class Meta:
        db_table = 'reserve_table'
        
class my(models.Model):
    Passenger_name=models.CharField(max_length=40)
    Email=models.CharField(max_length=40)
    Phone_number=models.CharField(max_length=40)
    Number_pass=models.CharField(max_length=40)
    Seat=models.CharField(max_length=40)
    class Meta:
        db_table = 'my_table'
    
    