from django.shortcuts import render, redirect
from .forms import CustomerForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm

# Create your views here.

@login_required(login_url = '/login')

def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

def add_emp(request):
    form = EmployeeForm
    submitted = False

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_emp')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'main/employee.html', {'form': form, 'submitted': submitted})


def add_customer(request):
    form = CustomerForm
    submitted = False

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_cust')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/customer.html', {'form': form, 'submitted': submitted})