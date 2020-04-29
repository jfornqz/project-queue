from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class medical_history(models.Model):
    occupation = models.CharField(max_length=255)
    congenital_disease = models.CharField(max_length=255)
    fname_emergency = models.CharField(max_length=255)
    lname_emergency = models.CharField(max_length=255)
    address_emergency = models.TextField()
    relationship_emergency = models.CharField(max_length=255)
    phone_emergency = models.CharField(max_length=10)
    account_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return 'medical_history: '  +' | '+ self.account_id.first_name +'  '+ self.account_id.last_name

class admission_note(models.Model):
    admission_no = models.IntegerField()
    patient_types = models.CharField(max_length=255)
    weight = models.IntegerField()
    height = models.IntegerField()
    pressure = models.IntegerField()
    drug_allergic = models.CharField(max_length=255)
    symptoms = models.TextField()
    create_date = models.DateField(auto_now=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'admission_note: ' + str(self.admission_no) +' | '+ str(self.patient)