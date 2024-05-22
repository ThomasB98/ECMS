from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserDeviceFrom
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import UserDevices
from django.http import JsonResponse
# Create your views here.


@login_required(login_url="/login")
def home(request):
    posts = UserDevices.objects.filter(author=request.user)
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        start_post_id = request.POST.get("post-start")
        stop_post_id = request.POST.get("post-end")
        if post_id:
            post = UserDevices.objects.filter(id=post_id).first()
            if post and post.author == request.user:
                post.delete()
        if start_post_id:
            print(start_post_id)
        if stop_post_id:
            print(stop_post_id)
    return render(request, 'Authentication/home.html', {"posts": posts})


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/sign_up.html', {"form": form})


@login_required(login_url="/login")
def AddUserDevices(request):
    if request.method == "POST":
        form = UserDeviceFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = UserDeviceFrom()

    return render(request, 'Authentication/addUserDevices.html', {"form": form})
