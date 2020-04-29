from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import formset_factory
from django import forms
from authen.models import Medical_Personal, Patient
from .models import admission_note, medical_history
from datetime import date, datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User

from django.db.models import Q
from django.contrib import messages

@login_required
@permission_required('userprofile.add_medical_history')
def patientprofile(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    admit = admission_note.objects.filter(patient_id=num)
    context = {
                'user': user,
                'patient': patient,
                'admit' : admit
            }
    try:
        m_history = medical_history.objects.get(account_id_id=num)
        context.update({'m_history' : m_history})
        have_mh = True
    except:
        have_mh = False


    if request.method == 'POST':
        if have_mh == True:
            m_history.occupation = request.POST.get('occupation')
            m_history.congenital_disease = request.POST.get('congenital_disease')
            m_history.fname_emergency = request.POST.get('fname_emergency')
            m_history.lname_emergency = request.POST.get('lname_emergency')
            m_history.address_emergency = request.POST.get('address_emergency')
            m_history.relationship_emergency = request.POST.get('relationship_emergency')
            m_history.phone_emergency = request.POST.get('phone_emergency')
            m_history.save()
        else:
            new_obj = medical_history.objects.create(
                occupation = request.POST.get('occupation'),
                congenital_disease = request.POST.get('congenital_disease'),
                fname_emergency = request.POST.get('fname_emergency'),
                lname_emergency = request.POST.get('lname_emergency'),
                address_emergency = request.POST.get('address_emergency'),
                relationship_emergency = request.POST.get('relationship_emergency'),
                phone_emergency = request.POST.get('phone_emergency'),
                account_id_id = num
            )
            context.update({'m_history' : new_obj})
        context.update({'msg' : 'บันทึกสำเร็จ!!!'})
    return render(request, 'userprofile/patientprofile.html', context)


# Create your views here.
@login_required
@permission_required('queuesystem.add_queue_system')
def editprofile(request):
    user = request.user
    patient = user.patient
    context = {
                'user': user,
                'patient': patient
            }
    if request.method == 'POST' and 'savepassword' in request.POST:
        if user.check_password(request.POST.get('password')) and request.POST.get('new_password')==request.POST.get('confirm_password'):
            user.set_password(request.POST.get('new_password'))
            user.save()
            user = authenticate(request, username=user.username, password=request.POST.get('new_password'))
            if user:
                login(request, user)
            context.update({'msg' : 'เปลี่ยนรหัสผ่านสำเร็จแล้ว'})
        else:
            context.update({'msgg' : 'รหัสผ่านไม่ตรงกัน กรุณาใส่รหัสผ่านให้ถูกต้อง'})

    elif request.method == 'POST' and 'saveprofile' in request.POST:
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        today = datetime.today()
        birth = datetime.strptime(request.POST.get('dob'), '%Y-%m-%d')
        if birth < today:
            patient.phone = request.POST.get('phone')
            patient.address = request.POST.get('address')
            patient.dob = birth
            patient.age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
            patient.save()
            context.update({'msg' : 'บันทึกสำเร็จ!!!'})
        else:
            context.update({'msgg' : 'กรุณากรอกข้อมูลให้ถูกต้อง'})

    return render(request, 'userprofile/editprofile.html', context)

@login_required
@permission_required('userprofile.add_medical_history')
def search(request):
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
                return render(request, 'userprofile/search.html', context)
            else:
                messages.error(request, 'No Patient found')

    return render(request, 'userprofile/search.html', context)



@login_required
@permission_required('userprofile.add_medical_history')
def admittedpatienthistory(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    admit = admission_note.objects.filter(patient_id=num)
    amount = admit.count()
    next_no = amount+1
    context = {
        'user' : user,
        'patient' : patient,
        'admit' : admit,
        'next_no' : next_no
    }
    if request.method == 'POST':
        admitted = admission_note.objects.create(
            admission_no = next_no,
            patient_types = request.POST.get('patient_types'),
            weight = request.POST.get('weight'),
            height = request.POST.get('height'),
            pressure = request.POST.get('pressure'),
            drug_allergic = request.POST.get('drug_allergic'),
            symptoms = request.POST.get('symptoms'),
            patient_id = patient.account_id_id
        )
        return redirect('patientprofile', num)
    return render(request, 'userprofile/admittedpatienthistorycreate.html', context)

@login_required
@permission_required('userprofile.add_medical_history')
def search_foradmitted(request):
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
                return render(request, 'userprofile/searchforadmitted.html', context)
            else:
                messages.error(request, 'No Patient found')

    return render(request, 'userprofile/searchforadmitted.html', context)