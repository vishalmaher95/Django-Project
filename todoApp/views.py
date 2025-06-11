from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from todoApp import models
from todoApp.models import Todo
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
     Unm=request.POST.get('username')
     email=request.POST.get('email')
     password=request.POST.get('password')
     print(Unm,email,password)
     my_user = User.objects.create_user(Unm,email,password)
     my_user.save()
     return redirect("/login")
    return render(request,'signup.html')

def loginn(request):
    error = None
    if request.method == 'POST':
       Unm=request.POST.get('username')
       password=request.POST.get('password')
       print(Unm,password)
       userr = authenticate(request,username=Unm,password=password)
       if userr is not None:
          login(request,userr)
          return redirect("/todopage")
       else:
           error = "Invalid username or password!" 
    return render(request,'loginn.html',{'error': error})

@login_required(login_url='/login')
def todopage(request):
    if request.method == 'POST':
       title=request.POST.get('title')
       print(title)
       obj =models.Todo(title=title,user=request.user)
       obj.save()
       res = models.Todo.objects.filter(user=request.user).order_by('-date')
       print(res)
       return redirect("/todopage",{'res' : res})
    
    res = models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request,'todopage.html',{'res' : res})

@login_required(login_url='/login')
def edit_todo(request,id):
    if request.method == 'POST':
       title=request.POST.get('title')
       print(title)
       obj =models.Todo.objects.get(id=id)
       obj.title=title
       obj.save()
       res = models.Todo.objects.filter(user=request.user).order_by('-date')
       print(res)
       return redirect("/todopage",{'obj' : obj})  
    obj=models.Todo.objects.get(id=id)
    res = models.Todo.objects.filter(user=request.user).order_by('-date')
    return render(request,'edit_todo.html',{'obj' : obj})

@login_required(login_url='/login')
def delete_todo(request,id):
   obj=models.Todo.objects.get(id=id)
   obj.delete()
   return redirect("/todopage")

def signout(request):
   logout(request)
   return redirect('/login')
   