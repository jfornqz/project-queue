import email
from builtins import object
from venv import create
from datetime import date, datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User, auth
from .models import Medical_Personal, Patient

from .forms import MedicalPersonalForm


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
            next_url = request.POST.get('next_url')
            group = request.user.groups.values_list('name', flat=True).first()
            print(group)
            if next_url:
                return redirect(next_url)
            elif group == "Patient":
                return redirect('main_patient')
            elif group == "Medical_Personnel":
                return redirect('main_medicalpersonnel')
            else:
                return redirect('index')
        else:
            context['error'] = 'Username หรือ Password ไม่ถูกต้อง!'
    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url
    return render(request, 'authen/login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')


def my_register(request):
    logout(request)
    context = {}
    msg = ''
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            pt = 'Patient'
            user = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('password1')

            )
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')

            group = Group.objects.get(name=pt)
            user.groups.add(group)

            user.save()

            today = datetime.today()
            birth = datetime.strptime(request.POST.get('dob'), '%Y-%m-%d')
            if birth < today:
                try:
                    patient = Patient.objects.create(
                        national_id=request.POST.get('national_id'),
                        name_title=request.POST.get('name_title'),
                        dob=request.POST.get('dob'),
                        gender='',
                        age=0,
                        blood_type=request.POST.get('blood_type'),
                        address=request.POST.get('address'),
                        phone=request.POST.get('phone'),
                        account_id=user,
                    )


                    if request.POST.get('name_title') == 'นาย' or request.POST.get('name_title') == 'เด็กชาย':
                        patient.gender = 'ชาย'
                    else:
                        patient.gender = 'หญิง'
                    patient.age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
                    patient.save()
                    return redirect('index')
                except:
                    user.delete()
                    context['error'] = 'กรอกข้อมูลไม่ถูกต้อง'
            else:
                user.delete()
                context['error'] = 'กรอกข้อมูลไม่ถูกต้อง'
        else:
            context['error'] = 'กรุณากรอก Password ให้ตรงกัน'
    else:
        user = User.objects.none()

    return render(request, 'authen/register.html', context)

@permission_required('userprofile.delete_medical_history')
def register_med(request):
    form = MedicalPersonalForm()
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            mp = 'Medical_Personnel'
            user = User.objects.create_user(
                request.POST.get('username'),
                request.POST.get('email'),
                request.POST.get('password1')

            )
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')

            group = Group.objects.get(name=mp)
            user.groups.add(group)

            user.save()
            try:
                form = MedicalPersonalForm(request.POST)
                if form.is_valid():
                    med = form.save(commit=False)
                    med.account_id = user
                    med.save()
                    return redirect('index')
                else:
                    user.delete()
                    context['error'] = 'กรอกข้อมูลไม่ถูกต้อง'
            except:
                user.delete()
                context['error'] = 'กรอกข้อมูลไม่ถูกต้อง'
        else:
            context['error'] = 'กรุณากรอก Password ให้ตรงกัน'
    else:
        user = User.objects.none()
    return render(request, 'authen/register_medicalpersonnel.html', {
        'form' : form
    })

@login_required
@permission_required('userprofile.add_medical_history')
def changepassword(request):
    user = request.user
    context = {
                'user': user,
        }
    if request.method == 'POST':
        if user.check_password(request.POST.get('password')) and request.POST.get('new_password')==request.POST.get('confirm_password'):
            user.set_password(request.POST.get('new_password'))
            user.save()
            user = authenticate(request, username=user.username, password=request.POST.get('new_password'))
            if user:
                login(request, user)
            return redirect('login')
        else:
            context['error'] = 'เปลี่ยนรหัสผ่านไม่สำเร็จ กรุณาใส่รหัสผ่านให้ถูกต้อง'
    return render(request, 'authen/changepassword.html',context=context)
