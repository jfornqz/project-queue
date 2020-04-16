from django.db import models
from authen.models import Patient, Medical_Personal

# Create your models here.
class Queue_System(models.Model):
    queue_id = models.IntegerField(primary_key=True)
    queue_no = models.IntegerField()
    time = models.TimeField(auto_now=False)
    date = models.DateField(auto_now=False)
    status = models.BooleanField(null=False)
    
class Appoinment(models.Model):
    app_id = models.IntegerField(primary_key=True)
    reason = models.IntegerField(max_length=255)        
    app_time = models.TimeField(auto_now=False)
    pt_id = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    me_id = models.ForeignKey(Medical_Personal, on_delete=models.CASCADE, null=False)

