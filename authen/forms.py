from django.forms import ModelForm
from django import forms
from .models import Medical_Personal

class MedicalPersonalForm(ModelForm):
    class Meta:
        model = Medical_Personal
        fields = ['position']
        CHOICES = (
            ("แพทย์" , "แพทย์"),
            ("พยาบาล" , "พยาบาล"),
            ("Staff" , "Staff")
        )
        labels = {
            'position' : ''
        }
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control required col-lg-5 d-block mx-auto'}, choices=CHOICES)
        }
