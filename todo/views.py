from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .forms import ToDoForms, Login, Register
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    try:
        user = request.session['user']
    except KeyError:
        user = None
    if user is None:
        return redirect("/login")
    else:
        form = ToDoForms()
        tasks = Task.objects.filter(user_id=user).values('pk', 'name')
        tasks = tasks.values('pk', 'name')
        context = {"form": form, "tasks": tasks}
        return render(request, 'index.html', context=context)


def create(request):
    if request.method == 'POST':
        user = request.session['user']
        form = ToDoForms(request.POST)
        task = Task(name=form.data.get('task'), user_id=user)
        Task.save(task)

        return redirect('/')


def login(request):
    form = Login()
    context = {"form": form}
    return render(request, 'login.html', context)


# Create your views here.
def auth(request):
    form = Login(request.POST)
    user_data = form.data
    email = user_data['email']
    password = user_data['password']
    if request.method == 'POST':
        user = User.objects.filter(email=email).values('password')
        try:
            passw = user[0]['password']
        except IndexError:
            passw = None
        if passw is not None and check_password(password, passw):
            user = User.objects.filter(email=email).values('pk')
            user = user[0]['pk']
            if user is not None:
                request.session['user'] = user
                return redirect("/")
        else:
            messages.info(request, 'E-mail or password incorrect')
            return redirect("/")


def logout(request):
    del request.session['user']
    return redirect('/')


def new(request):
    form = Register()
    context = {"form": form}
    return render(request, "register.html", context)


def register(request):
    form = Register(request.POST)
    user_data = form.data

    username = user_data['username']
    email = user_data['email']
    password = user_data['password']

    if request.method == 'POST':
        user = User.objects.filter(email=email).values('password')
        try:
            user = user[0]['password']
        except IndexError:
            user = None

        if user is None:
            new_user = User(username=username, email=email, password=make_password(password))
            User.save(new_user)

            user = User.objects.filter(email=email).values('pk')
            request.session['user'] = user[0]['pk']
            return redirect("/")
        else:
            messages.error(request, 'This email is already in use')
            return redirect("/newaccount")


def remove(request, task_id):
    print(task_id)
    task = Task.objects.get(pk=task_id)
    print(task)
    task.delete()
    return redirect('/')
