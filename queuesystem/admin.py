from django.contrib import admin
from queuesystem.models import Appoinment, Queue_System
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(Appoinment)
admin.site.register(Queue_System)
admin.site.register(Permission)