from django.shortcuts import render
import random
from builtins import id, object
from fnmatch import filter
from os.path import isdir
from re import search
from urllib import response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.admin import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request




# Create your views here.
def index(request):
    context = {}
    return render(request, 'queuesystem/index.html', context)

def my_login(request):
    context = {}
    return render(request, 'queuesystem/login.html', context)

def my_logout(request):
    context = {}
    return render(request, 'queuesystem/login.html', context)

def my_register(request):
    context = {}
    return render(request, 'queuesystem/register.html', context)

def change_password(request):
    context = {}
    return render(request, 'queuesystem/changepassword.html', context)