from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from todoApp import models
from todoApp.models import Todo

def signup(request):
    if request.method == 'POST':
     Unm=request.POST.get('username')
     email=request.POST.get('email')
     password=request.POST.get('password')
     print(Unm,email,password)
     my_user = User.objects.create_user(Unm,email,password)
     my_user.save()
    return render(request,'signup.html')