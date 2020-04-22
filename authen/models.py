from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    national_id = models.CharField(max_length=13, unique=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    name_title = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False)
    address = models.TextField()
    account_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Medical_Personal(models.Model):
    position = models.CharField(max_length=255)
    account_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)