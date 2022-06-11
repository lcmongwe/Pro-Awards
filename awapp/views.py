from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from .forms import *
# from django.core.mail import send_mail
# from django.conf import settings


def home(request):
    posts=Post.objects.all()
    
    
    return render(request, 'home.html', {'posts': posts,'profile': profile})


def landing(request):
    
    return render(request, 'landing.html', {})

def profile(request,pk):
    posterr=Profile.objects.get(id=pk)
    posts=posterr.poster.all()
    posts_count=posts.count()

    return render(request, 'profile.html', {'posts': posts,'posterr': posterr,'posts_count': posts_count})

def create_post(request):
    return render(request, 'post.html', {})