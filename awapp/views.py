from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from django.contrib import messages
from .forms import *



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
    form=CreatePostForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,(' posted successfully!'))
        
        return redirect('home')
    return render(request, 'post.html', {})