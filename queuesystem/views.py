
from django.shortcuts import redirect, render

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

def appointment_create(request):
    context = {}
    return render(request, 'queuesystem/appointmentcreate.html', context)

def main_appoitment(request):
    context = {}
    return render(request, 'queuesystem/mainappointment.html', context)


