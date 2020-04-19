from django.shortcuts import render
from django.contrib.auth.models import User
from django.forms import formset_factory
from django import forms
from authen.models import Medical_Personal, Patient, Admin


# Create your views here.
def editprofile(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    context = {
        'user': user,
        'patient': patient
    }
    return render(request, 'editprofilehistory/editprofile.html', context)

def search(request):
    search = request.POST.get('search', '')
    first_name_patient = User.objects.filter(first_name__icontains=search)
    id_patient = User.objects.filter(id__icontains=search)
    result = zip(id_patient, first_name_patient)
    # if id_patient.exists():
    #    result = zip(id_patient, first_name_patient)
    context = {
        'firstname_patient' : first_name_patient,
        'id_patient' : id_patient,
        'result' : result,
        'search' : search,


    }
    return render(request, 'editprofilehistory/search.html', context)