from django.urls import path
from . import views

urlpatterns = [
    
    path('login/',  views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.my_register, name='register'),
    path('change_password/', views.change_password, name='change_password')

]