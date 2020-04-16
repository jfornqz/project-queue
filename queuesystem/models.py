from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Queue_System(models.Model):
    queue_id = models.IntegerField(primary_key=True)
    queue_no = models.IntegerField()
    time = models.TimeField(auto_now=False)
    date = models.DateField(auto_now=False)
    status = models.BooleanField(null=False)

class Patient(models.Model):
    pt_id = models.IntegerField(primary_key=True) 
    age = models.IntegerField(max_length=3)
    date_of_birth = models.DateField(auto_now=False)
    contact = models.CharField(max_length=255) 
    queue_id = models.ForeignKey(Queue_System, on_delete=models.CASCADE, null=False) 
    

class Medical_Personal(models.Model):
    me_id = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=255)
    queue_id = models.ForeignKey(Queue_System, on_delete=models.CASCADE, null=False)
    
class Appoinment(models.Model):
    app_id = models.IntegerField(primary_key=True)
    reason = models.IntegerField(max_length=255)        
    app_time = models.TimeField(auto_now=False)
    pt_id = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    me_id = models.ForeignKey(Medical_Personal, on_delete=models.CASCADE, null=False)

class Account(models.Model): 
    account_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    pt_id = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    me_id = models.ForeignKey(Medical_Personal, on_delete=models.CASCADE, null=False)

class Admin(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)