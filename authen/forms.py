from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Medical_Personal

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields  = ['username','password','first_name','last_name','email']
        labels = {
            'username': 'Username',
            'password': 'Password',
            'first_name': 'ชื่อ',
            'last_name': 'นามสกุล',
            'email': 'อีเมล'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control required col-lg-5 d-block mx-auto'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control required col-lg-5 d-block mx-auto'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control required col-lg-5 d-block mx-auto'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control required col-lg-5 d-block mx-auto'}),
            'email': forms.TextInput(attrs={'class': 'form-control required col-lg-5 d-block mx-auto'}),
        }

class MedicalPersonForm(ModelForm):
    class Meta:
        CHOICES = (
            ("แพทย์" , "แพทย์"),
            ("พยาบาล" , "พยาบาล"),
            ("Staff" , "Staff")
        )
        model = Medical_Personal
        fields = ['position']
        labels = {
            'position' : 'Job Position'
        }
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control required col-lg-5 d-block mx-auto'}, choices=CHOICES)
        }

