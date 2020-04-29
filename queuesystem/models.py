from django.db import models
from authen.models import Patient, Medical_Personal

# Create your models here.
class Queue_System(models.Model):
    queue_id = models.IntegerField(primary_key=True)
    queue_no = models.IntegerField()
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20)
    create_by = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    doctor = models.ForeignKey(Medical_Personal, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return 'Queue_id: ' + str(self.queue_id) + ' by ' + str(self.create_by) 

class Appointment(models.Model):
    app_id = models.IntegerField(primary_key=True)
    reason = models.CharField(max_length=255)     
    create_date = models.DateField(auto_now=True)
    next_date = models.DateField(auto_now=False)   
    app_time = models.TimeField(auto_now=False)
    pt_id = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    me_id = models.ForeignKey(Medical_Personal, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return 'Appointment: ' + str(self.app_id) +'  '+ str(self.pt_id)


