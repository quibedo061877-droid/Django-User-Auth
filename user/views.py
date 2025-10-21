from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page!")

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return HttpResponse("Registration successful!")
                # messages.success(request, "Registration successful!")
                # return redirect('login')
            except:
                messages.error(request, "Username already exists.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'registration/register.html')
