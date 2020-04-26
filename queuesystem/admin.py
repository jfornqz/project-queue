from django.contrib import admin
from queuesystem.models import Appointment, Queue_System
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Queue_System)
admin.site.register(Permission)