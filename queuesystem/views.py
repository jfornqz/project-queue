
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import formset_factory
from django import forms
from authen.models import Medical_Personal, Patient
from datetime import date, datetime



# Create your views here.
def index(request):
    context = {}
    return render(request, 'queuesystem/index.html', context)

def main_patient(request):
    context = {}
    return render(request, 'queuesystem/main_patient.html', context)

def main_medicalpersonnel(request):
    context = {}
    return render(request, 'queuesystem/main_medicalpersonnel.html', context)

def run_queue(request):
    context = {}
    return render(request, 'queuesystem/runqueue.html', context)

def remaining_queue(request):
    context = {}
    return render(request, 'queuesystem/remainingqueue.html', context)

def generate_queue(request):
    context = {}
    return render(request, 'queuesystem/generatequeue.html', context)

def appoitment_check(request):
    context = {}
    return render(request, 'queuesystem/appoitmentcheck.html', context)

def appointment_create(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    context = {
                'user': user,
                'patient': patient
            }
    return render(request, 'queuesystem/appointmentcreate.html', context)

def search_appointment(request):
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
    return render(request, 'queuesystem/searchappointment.html', context)


def main_appointment(request):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    context = {
                'user': user,
                'patient': patient
            }
    return render(request, 'queuesystem/mainappointment.html', context)


