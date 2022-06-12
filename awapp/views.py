from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    posts=Post.objects.all()
    return render(request, 'home.html', {'posts': posts,'profile': profile})


def landing(request):
    
    return render(request, 'landing.html', {})

@login_required(login_url='login')
def profile(request,pk):
    user=Profile.objects.get(id=pk)
    posterr=Profile.objects.get(id=pk)
    posts=posterr.poster.all()
    posts_count=posts.count()

    return render(request, 'profile.html', {'posts': posts,'posterr': posterr,'posts_count': posts_count,'user': user})


@login_required(login_url='login')
def create_post(request):
    form=CreatePostForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,(' posted successfully!'))
        
        return redirect('home')
    return render(request, 'post.html', {'form': form})



@login_required(login_url='login')
def update_post( request,pk):
    post=Post.objects.get(id=pk)
    form=CreatePostForm(request.POST,request.FILES,intance=post)

    return render(request, 'post.html', {'form': form,'post':post})


@login_required(login_url='login')
def delete_post( request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete.html', {'post':post})


def create_profile(request,user_id):
    user=User.objects.get(id=user_id)
    form=ProfileForm(request.POST,request.FILES )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,(' posted successfully!'))
        
        return redirect('home')
    return render(request, 'update_profile.html',{'user':user,'form':form})

def review(request,post_id ):
    user = request.user
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
        form=ReviewForm(request.POST )
        if form.is_valid():
            form=form.save(commit=False)
            form.post=post
            form.save()
            return redirect('home')
    else:
        form=ReviewForm()

    return render(request, 'review.html',{'user':user,'form':form})
