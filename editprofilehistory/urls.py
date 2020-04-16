from django.urls import path
from . import views

urlpatterns = [
    
      path('editprofile/',  views.editprofile, name='editprofile'),
]