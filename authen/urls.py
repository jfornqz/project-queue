from django.urls import path
from . import views

urlpatterns = [
    
    path('login/',  views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.my_register, name='register'),
    path('register_medicalpersonnel/', views.register_med, name='register_med'),
    path('changepassword/', views.changepassword, name='changepassword'),

]