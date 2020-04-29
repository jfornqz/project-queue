from django.forms import ModelForm
from .models import Medical_Personal

class MedicalPersonalForm(ModelForm):
    class Meta:
        model = Medical_Personal
        fields = ['position']