from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from .forms import *
# from django.core.mail import send_mail
# from django.conf import settings


def home(request):
    posts=Post.objects.all()
    
    return render(request, 'home.html', {'posts': posts})


def landing(request,pk):
    user=Profile.objects.get(id=pk)
    
    return render(request, 'landing.html', {'user':user})

def profile(request):
    return render(request, 'profile.html', {})
