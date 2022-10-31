from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Employee, Customer

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'emp_id': '',
            'emp_name': '',
            'emp_pay_rate': '',
            'emp_weekly_hours': '',
            'emp_start_date': '',
            'emp_dob': '',
            'emp_email': '',
        }

        widgets = {
            'emp_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}),
            'emp_pay_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pay Rate'}),
            'emp_weekly_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weekly Hours'}),
            'emp_start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
            'emp_dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            'emp_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'cust_id': '',
            'cust_name': '',
            'cust_email': '',
            'cust_dob': '',
         }

        widgets = {
            'cust_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer ID'}),
            'cust_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'cust_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'cust_dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
         }
