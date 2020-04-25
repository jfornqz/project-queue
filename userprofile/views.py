from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import formset_factory
from django import forms
from authen.models import Medical_Personal, Patient
from datetime import date, datetime
from .filters import UserFilter




# Create your views here.
def editprofile(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
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
            context.update({'msg' : 'กรุณากรอกข้อมูลให้ถูกต้อง'})

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
            context.update({'msg' : 'กรุณากรอกข้อมูลให้ถูกต้อง'})

    elif request.method == 'POST' and 'savepicture' in request.POST:
        patient.picture = request.FILES['picture']
        patient.save()
    return render(request, 'userprofile/editprofile.html', context)

# def search(request):
#     search = request.POST.get('search', '')
#     first_name_patient = User.objects.filter(first_name__icontains=search)
#     id_patient = User.objects.filter(id__icontains=search)
#     result = zip(id_patient, first_name_patient)
#     # if id_patient.exists():
#     #    result = zip(id_patient, first_name_patient)
#     context = {
#         'firstname_patient' : first_name_patient,
#         'id_patient' : id_patient,
#         'result' : result,
#         'search' : search,


#     }
#     return render(request, 'userprofile/search.html', context)
def search(request):
    search = User.objects.all()
    user_filter = UserFilter(request.POST, queryset=search)
    print(search)
    
    return render(request, 'userprofile/search.html', {'filter': user_filter})

def admittedpatienthistory(request, num):
    user = User.objects.get(pk=num)
    patient = Patient.objects.get(account_id_id=num)
    context = {
        'user' : user,
        'patient' : patient

    }
    return render(request, 'userprofile/admittedpatienthistorycreate.html', context)

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