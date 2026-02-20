from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def create_user(request):
    if request.method == 'POST':
        # Handle user creation logic here
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login_user')
    return render(request, 'users/create_user.html')

def login_user(request):
    if request.method == 'POST':
        # Handle user login logic here
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login_user.html')