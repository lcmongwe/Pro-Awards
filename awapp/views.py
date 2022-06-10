from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from .forms import *
# from django.core.mail import send_mail
# from django.conf import settings


def home(request):
    
    return render(request, 'home.html', {})


def landing(request):
    
    return render(request, 'landing.html', {})

