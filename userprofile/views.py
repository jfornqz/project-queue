from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import formset_factory
from django import forms
from authen.models import Medical_Personal, Patient
from datetime import date, datetime


# Create your views here.

# 2 group > ผู้ป่วย / บุลคากรคลินิก
# ผู้ป่วย > Edit Profile / Change password
# บุลคากรคลินิก > Patient Profile / Medical History / Admission note
def editprofile(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    context = {
                'user': user,
                'patient': patient
            }
    if request.method == 'POST':
        if user.check_password(request.POST.get('password')) and request.POST.get('new_password')==request.POST.get('confirm_password'):
            user.set_password(request.POST.get('new_password'))
            user.save()
            user = authenticate(request, username=user.username, password=request.POST.get('new_password'))
            if user:
                login(request, user)
            context.update({'msg' : 'เปลี่ยนรหัสผ่านสำเร็จแล้ว'})
        else:
            context.update({'msg' : 'กรุณากรอกข้อมูลให้ถูกต้อง'})
    return render(request, 'userprofile/editprofile.html', context)

# บุคลากรเห็นเท่านั้น
# ค้นหาผู้ป่วยเพื่อที่จะเข้าหน้า Patient Profile / Medical History / Admission note
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
    return render(request, 'userprofile/search.html', context)

# บุคลากรเห็นเท่านั้น
# หน้าเพิ่ม ประวัติเข้ารับการรักษาของผู้ป่วย admittedpatienthistorycreate 
def admittedpatienthistory(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    context = {
        'user' : user,
        'patient' : patient

    }
    return render(request, 'userprofile/admittedpatienthistorycreate.html', context)

# บุคลากรเห็นเท่านั้น
# ค้นหาผู้ป่วยเพื่อที่จะเข้าหน้า admittedpatienthistorycreate 
def search_foradmitted(request):
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
    return render(request, 'userprofile/searchforadmitted.html', context)