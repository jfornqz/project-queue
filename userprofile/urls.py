from django.urls import path
from . import views
from django_filters.views import FilterView



urlpatterns = [
      path('editprofile/',  views.editprofile, name='editprofile'),
      path('patientprofile/<int:num>/',  views.patientprofile, name='patientprofile'),
      path('search/', views.search, name='search'),
      path('add_admittedpatienthistory/<int:num>/',  views.admittedpatienthistory, name='admittedpatienthistory'),
      path('search_admitted/',  views.search_foradmitted, name='search_foradmitted'),
]