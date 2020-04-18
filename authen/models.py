from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True) 

class Patient(models.Model):
    age = models.IntegerField(max_length=3)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    name_title = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False)
    address = models.TextField()
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)

class Medical_Personal(models.Model):
    position = models.CharField(max_length=255)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)