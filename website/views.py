from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def home(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request,username=username,password=password)
          if user is not None:
               login(request,user)
               messages.success(request,"You have been successfully logged in!!")
               return redirect('home')
          else:
               messages.success(request,"Wrong password or username :(")
               return redirect('home')
     else:
          return render(request, 'home.html', {})

def logout_user(request):
     logout(request)
     messages.success(request,"You have been successfully logged out!!")
     return redirect('home')

def register_user(request):
     return render(request, 'register.html', {})

# Create your views here.
