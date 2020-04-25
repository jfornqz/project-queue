from django.contrib.auth.models import User
import django_filters
from django import forms

class UserFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', ]