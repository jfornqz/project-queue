import email
from builtins import object
from venv import create

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
    context = {}
    msg = ''
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('password1'),
            )
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            print(user.id)
            patient = Patient.objects.create(
                name_title=request.POST.get('name_titles'),
                dob=request.POST.get('dob'),
                gender=request.POST.get('gender'),
                age=request.POST.get('age'),
                address=request.POST.get('address'),
                phone=request.POST.get('phone'),
                account_id=User.objects.get(pk=user.id)
            )
            return redirect('login')
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
