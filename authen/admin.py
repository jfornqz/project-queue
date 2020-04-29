from django.contrib import admin
from authen.models import Patient, Medical_Personal

# Register your models here.

class MedicalPersonalAdmin(admin.ModelAdmin):
    list_display = [
        'position',
        'account_id'
    ]

admin.site.register(Patient)
admin.site.register(Medical_Personal, MedicalPersonalAdmin)
