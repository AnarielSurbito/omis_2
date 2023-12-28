import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddExpForm, AddRecordForm
from .models import Event, Exponents


def home(request):
    events = Event.objects.all()
    exponents = Exponents.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In, you are greate")
            return redirect('home')
        else:
            messages.success(request, "Try Again, Because there is an error")
            return redirect('home')
    else:
        return render(request, 'home.html', {'events':events})


def logout_user(request):
    logout(request)
    messages.success(request, "Bye")
    return redirect('home')


def notif(request):
    #date = datetime.date()
    if request.user.is_authenticated:
        events = Event.objects.all()
        return render(request, 'notif.html', {'events': events})

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You register")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form': form})


def my_events(request):
    events = Event.objects.filter(my_eve=True)
    exponents = Exponents.objects.all()
    return render(request, 'myevents.html', {'events':events})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Event.objects.get(name=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Залогиньтесь или Зарегестрируйтесь")
        return redirect('home')

def customer_exp(request, pk):
    customer_exp = Exponents.objects.get(name=pk)
    return render(request, 'exponent.html', {'customer_exp': customer_exp})

def my_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Event.objects.get(name=pk, my_eve=True)
        return render(request, 'myrecord.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Залогиньтесь или Зарегестрируйтесь")
        return redirect('home')

def my_exp(request, pk):
    customer_exp = Exponents.objects.get(name=pk, my_exp=True)
    return render(request, 'myexponents.html', {'customer_exp': customer_exp})


def del_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Event.objects.get(name=pk)
        delete_it.delete()
        messages.success(request, "Выставка удалена")
        return redirect('home')
    else:
        messages.success(request, "Залогиньтесь или Зарегестрируйтесь")
        return redirect('home')

def del_exp(request, pk):
    delete_it = Exponents.objects.get(name=pk)
    delete_it.delete()
    messages.success(request, "Экспонат удалён")
    return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Добавлено")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Залогиньтесь или Зарегестрируйтесь")
        return redirect('home')


def add_exp(request):
    form = AddExpForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_exp = form.save()
                messages.success(request, "Добавлено")
                return redirect('home')
        return render(request, 'add_exp.html', {'form': form})
    else:
        messages.success(request, "Залогиньтесь или Зарегестрируйтесь")
        return redirect('home')
