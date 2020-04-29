from rest_framework import serializers

from .models import Queue_System

class QueueSystemSerializer(serializers.ModelSerializer):
    doctor_firstname = serializers.ReadOnlyField(source='doctor.account_id.first_name')
    doctor_lastname = serializers.ReadOnlyField(source='doctor.account_id.last_name')

    patient_firstname = serializers.ReadOnlyField(source='create_by.account_id.first_name')
    patient_lastname = serializers.ReadOnlyField(source='create_by.account_id.last_name')
    class Meta:
        model = Queue_System
        fields = ['queue_id', 'queue_no', 'status', 'doctor_firstname', 'doctor_lastname', 'patient_firstname', 'patient_lastname']
