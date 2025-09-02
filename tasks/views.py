from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import models
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# User signup
def signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = forms.SignUpForm()

    return render(request, 'tasks/signup.html', {'form': form})


# User login
def login_view(request):
    
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            xx = user.username
            print(xx)
            if user is not None:
                login(request, user)
                return redirect('firstpage')
            else:
                return render(request, 'tasks/login.html', {
                    'form': form,
                    'error': 'Invalid username or password'
                })
    else:
        form = forms.LoginForm()

    return render(request, 'tasks/login.html', {'form': form})



def firstpage(request):
    return render(request, 'tasks/open.html')



# Task list (only for logged in user)
@login_required
def my_todo_view(request):
    tasks = models.Task.objects.filter(user=request.user)
    return render(request, 'tasks/list.html', {'tasks': tasks})


# Create task
@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('my_todo_view')
    else:
        form = forms.TaskForm()

    return render(request, 'tasks/create.html', {'form': form})

from .models import Task

# Edit task
@login_required
def edit_task_view(request, pk):
    # Get the task for this user
    task = get_object_or_404(models.Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('my_todo_view')
    else:
        form = forms.TaskForm(instance=task)
        print(pk)
    return render(request, 'tasks/create.html', {'form': form}) 


# Delete task
from django.shortcuts import get_object_or_404, redirect
from . import models

def delete_task_view(request, pk):
    task = get_object_or_404(models.Task, pk=pk, user=request.user)  
    task.delete()
    return redirect('my_todo_view')

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('firstpage')

def alert(request):
    return render(request, 'tasks/alert.html')