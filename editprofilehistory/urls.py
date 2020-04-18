from django.urls import path
from . import views

urlpatterns = [
      path('editprofile/<int:num>/',  views.editprofile, name='editprofile'),
      path('search/',  views.search, name='search'),
]