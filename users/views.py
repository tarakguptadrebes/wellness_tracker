from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def create_user(request):
    if request.method == 'POST':
        # Handle user creation logic here
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            pass
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'User created successfully')
            return redirect('login_user')
    return render(request, 'users/create_user.html')

def login_user(request):
    if request.method == 'POST':
        # Handle user login logic here
        pass
    return render(request, 'users/login_user.html')