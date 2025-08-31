from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import models
from . import forms





# User signup
def signup_view(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully")
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
def my_todo_view(request):
    tasks = models.Task.objects.filter(user=request.user)
    return render(request, 'tasks/list.html', {'tasks': tasks})


# Create task
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


# Edit task
def edit_task_view(request, pk):
    task = get_object_or_404(models.Task, pk=pk, user=request.user)

    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)
            updated_task.user = request.user   # 🔑 ensure correct user
            updated_task.save()
            return redirect('my_todo_view')
    else:
        form = forms.TaskForm(instance=task)

    return render(request, 'tasks/create.html', {'form': form})


# Delete task
from django.shortcuts import get_object_or_404, redirect
from . import models

def delete_task_view(request, pk):
    task = get_object_or_404(models.Task, pk=pk, user=request.user)  
    task.delete()
    return redirect('my_todo_view')

