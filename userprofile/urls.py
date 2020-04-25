from django.urls import path
from . import views
from django_filters.views import FilterView



urlpatterns = [
      path('editprofile/<int:num>/',  views.editprofile, name='editprofile'),
      path('search/', views.search, name='search'),
      path('add_admittedpatienthistory/<int:num>/',  views.admittedpatienthistory, name='admittedpatienthistory'),
      path('search_admitted/',  views.search_foradmitted, name='search_foradmitted'),
]