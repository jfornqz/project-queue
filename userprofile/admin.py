from django.contrib import admin
from userprofile.models import medical_history, admission_note
# Register your models here.

admin.site.register(medical_history)
admin.site.register(admission_note)
