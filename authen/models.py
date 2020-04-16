from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    account_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 

class Patient(models.Model):
    pt_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    age = models.IntegerField(max_length=3)
    date_of_birth = models.DateField(auto_now=False)
    phone = models.CharField(max_length=255) 

class Medical_Personal(models.Model):
    me_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    position = models.CharField(max_length=255)