import email
from builtins import object
from venv import create
from datetime import date, datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Medical_Personal, Patient


# Create your views here.
def my_login(request):
    logout(request)
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user: 
            login(request, user)
            return redirect('index')
        else:
            context['error'] = 'Username หรือ Password ไม่ถูกต้อง!'
    return render(request, 'authen/login.html', context)

def my_logout(request):
    logout(request)
    return redirect('login')

def my_register(request):
    logout(request)
    context = {}
    msg = ''
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('password1')
            )
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()

            try:
                patient = Patient.objects.create(
                    national_id=request.POST.get('national_id'),
                    name_title=request.POST.get('name_title'),
                    dob=request.POST.get('dob'),
                    gender='',
                    age=0,
                    address=request.POST.get('address'),
                    phone=request.POST.get('phone'),
                    account_id=user
                )
                if request.POST.get('name_title') == 'นาย' or request.POST.get('name_title') == 'เด็กชาย':
                    patient.gender = 'ชาย'
                else:
                    patient.gender = 'หญิง'
                birth = datetime.strptime(patient.dob, '%Y-%m-%d')
                today = date.today()
                patient.age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
                patient.save()
                return redirect('index')
            except:
                user.delete()
                context['error'] = 'กรอกข้อมูลไม่ถูกต้อง'
        else:
            context['error'] = 'กรุณากรอก Password ให้ตรงกัน'
    else:
        user = User.objects.none()

    return render(request, 'authen/register.html', context)

def register_med(request):
    context = {}
    return render(request, 'authen/register_medicalpersonnel.html', context)


def change_password(request):
    context = {}
    return render(request, 'authen/changepassword.html', context)
