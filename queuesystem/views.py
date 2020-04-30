
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import formset_factory
from django import forms
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from authen.models import Medical_Personal, Patient
from .models import Queue_System, Appointment
from datetime import date, datetime
from django.db.models import Q
from django.contrib import messages

# API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Serializer
from .serializers import QueueSystemSerializer


# Create your views here.
def index(request):
    context = {}
    return render(request, 'queuesystem/index.html', context)

# ผู้ป่วยเห็นเท่านั้น
# index ผู้ป่วย (เด้งมาจากเวลาผู้ป่วย login)
@login_required
@permission_required('queuesystem.add_queue_system')
def main_patient(request):
    context = {}
    user = request.user
    try:
        my_queue = Queue_System.objects.get(create_by_id=user.id, status='waiting')
        context.update({
            'my_queue' : my_queue
        })
        try:
            doctor = User.objects.get(pk=my_queue.doctor_id)
            context.update({'doctor' : doctor})
        except:
            pass
    except:
        pass
    context.update({
        'user' : user
    })
    return render(request, 'queuesystem/main_patient.html', context)

# บุคลากรคลินิกเห็นเท่านั้น
# index บุคลากรคลินิก (เด้งมาจากเวลาบุคลากรคลินิก login)
@login_required
@permission_required('userprofile.add_medical_history')
def main_medicalpersonnel(request):
    context = {}
    return render(request, 'queuesystem/main_medicalpersonnel.html', context)


class RunQueueView(APIView):

    def get(self, request):
        today = datetime.today()
        queue = Queue_System.objects.filter(date=today)

        serializer = QueueSystemSerializer(queue, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.get('queue')

        queue = Queue_System.objects.get(queue_id=data['queue_id'])

        if queue.status == 'called':
            queue.status = 'finished'
            queue.save()
        elif queue.status == 'waiting':
            queue.status = 'called'
            queue.save()

        serializer = QueueSystemSerializer(queue)
        return Response(serializer.data, status=status.HTTP_200_OK)

# บุคลากรคลินิก เห็นเท่านั้น
# รันคิว
@login_required
@permission_required('userprofile.add_medical_history')
def run_queue(request):
    context = {}
    today = date.today()

    queue = Queue_System.objects.filter(date=today)
    patient = User.objects.filter(groups__name='Patient')
    doctor = User.objects.filter(groups__name='Medical_Personnel')
    context.update({
        'queue' : queue,
        'patient' : patient,
        'doctor' : doctor,
        'today' : today
    })

    return render(request, 'queuesystem/runqueue.html', context)

# บุลคากรคลินิก เห็นเท่านั้น
# แสดงคิวที่เหลืออยู่
@login_required
@permission_required('userprofile.add_medical_history')
def remaining_queue(request):
    context = {}
    today = datetime.today()
    queue_remain = Queue_System.objects.filter(date=today, status='waiting').count()
    each_queue = Queue_System.objects.filter(date=today, status='waiting')
    
    context.update({
        'each_queue' : each_queue,
        'queue_remain' : queue_remain,
        
    })
    return render(request, 'queuesystem/remainingqueue.html', context)

# ผู้ป่วยเห็นเท่านั้น
# หน้าก่อนจะเข้าสู่รับคิว จะต้องเช็คผู้ป่วยก่อน ว่ามีนัดกับแพทย์หรือไม่
@login_required
@permission_required('queuesystem.add_queue_system')
def before_generatequeue(request):
    context = {}
    med_person = User.objects.filter(groups__name='Medical_Personnel')
    doctor = Medical_Personal.objects.filter(position='แพทย์')
    context = {
        'med_person' : med_person,
        'doctor' : doctor,
    }
    user = request.user
    today = datetime.today()
    queue = Queue_System.objects.filter(date=today)
    amount = queue.count()
    latest = queue.filter(create_by_id=user.id, status='waiting')
    next_queue = amount+1
    if request.method == 'POST':
        if latest.count() == 0:
            if request.POST.get('type') == "มีนัด":
                my_queue = Queue_System.objects.create(
                    queue_no = next_queue,
                    status = 'waiting',
                    create_by_id = user.id,
                    doctor_id = request.POST.get('med_id')
                )
            else:
                my_queue = Queue_System.objects.create(
                    queue_no = next_queue,
                    status = 'waiting',
                    create_by_id = user.id
                )
        return redirect('generate_queue')
    return render(request, 'queuesystem/before_generatequeue.html', context)


# ผู้ป่วยเห็นเท่านั้น
# รับคิว
@login_required
@permission_required('queuesystem.add_queue_system')
def generate_queue(request):
    context = {}
    user = request.user
    today = datetime.today()
    queue = Queue_System.objects.filter(date=today)
    amount = queue.count()
    latest = queue.filter(create_by_id=user.id, status='waiting')
    next_queue = amount+1
    context = {
        'my_queue' : latest.get(create_by_id=user.id, status='waiting')
    }
    return render(request, 'queuesystem/generatequeue.html', context)

# ผู้ป่วยเห็นเท่านั้น
# หน้าเช็คการนัดของผู้ป่วย (แสดงการนัดทั้งหมดของผู้ป่วย) มีการนัดทั้งหมดของผู้ป่วย คลิ๊กไปเข้าจะเป็นหน้า main_appointment
@login_required
@permission_required('queuesystem.add_queue_system')
def appointment_check(request):
    user = request.user
    context = {
        'user' : user
    }
    name_list = []
    appointment = Appointment.objects.filter(pt_id_id=user.id)
    if appointment:
        for i in appointment:
            med = Medical_Personal.objects.get(account_id_id=i.me_id_id)
            med_name = med.account_id.first_name+' '+med.account_id.last_name
            name_list.append(med_name)
        my_list = zip(appointment, name_list)
        context.update({
            'appointment' : appointment,
            'name_list' : name_list,
            'my_list' : my_list
            })
    else:
        context.update({
            'none_data': 'ไม่มีการนัดหมาย'
        })
    return render(request, 'queuesystem/appointmentcheck.html', context)

# บุคลากรคลินิกเห็นเท่านั้น
# หน้าสร้างการนัด
@login_required
@permission_required('userprofile.add_medical_history')
def appointment_create(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    doctor = Medical_Personal.objects.filter(position='แพทย์')
    med_person = User.objects.filter(groups__name='Medical_Personnel')
    today = date.today()
    context = {
                'user': user,
                'patient': patient,
                'med_person' : med_person,
                'doctor' : doctor,
                'today' : today
            }
    if request.method == 'POST':
        new_obj = Appointment.objects.create(
            reason = request.POST.get('reason'),
            next_date = request.POST.get('next_date'),
            app_time = request.POST.get('app_time'),
            me_id_id = request.POST.get('med_person'),
            pt_id_id = user.id
        )
    return render(request, 'queuesystem/appointmentcreate.html', context)

# บุคลากรคลินิกดูได้เท่านั้น
# ค้นหารายชื่อผู้ป่วย เพื่อสร้างการนัด (next page > appointmentcreate)
@login_required
@permission_required('userprofile.add_medical_history')
def search_appointment(request):
    Keep_patient = User.objects.filter(groups__name='Patient').order_by('id')
    context = {
        'pt': Keep_patient,
        'check': 1
    }

    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = User.objects.filter(Q(id__icontains=search)|
                                        Q(first_name__icontains=search)|
                                        Q(last_name__icontains=search),
                                        groups__name='Patient'
                                        ).order_by('id')

            if match:
                context = {
                    'match': match
                }
                return render(request, 'queuesystem/searchappointment.html', context)
            else:
                messages.error(request, 'No Patient found')

    return render(request, 'queuesystem/searchappointment.html', context)

# ผู้ป่วยเห็นเท่านั้น
# หน้า main ของ appointment เวลาผู้ป่วยดูรายละเอียดการนัด
@login_required
@permission_required('queuesystem.add_queue_system')
def main_appointment(request, num):
    user = request.user
    patient = Patient.objects.get(account_id_id=user.id)
    appointment = Appointment.objects.get(app_id=num)
    med = Medical_Personal.objects.get(account_id_id=appointment.me_id_id)
    med_firstname = med.account_id.first_name
    med_lastname = med.account_id.last_name
    context = {
                'user': user,
                'patient': patient,
                'appointment' : appointment,
                'med_firstname' : med_firstname,
                'med_lastname' : med_lastname
            }
    return render(request, 'queuesystem/mainappointment.html', context)


