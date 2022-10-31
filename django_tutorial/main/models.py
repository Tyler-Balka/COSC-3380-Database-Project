from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField('Employee ID', max_length = 3)
    emp_name = models.CharField('Employee Name', max_length = 50)
    emp_pay_rate = models.CharField('Pay Rate', max_length = 6)
    emp_weekly_hours = models.DecimalField('Weekly Hours', max_digits = 3, decimal_places = 1)
    emp_start_date = models.DateField('Employee Start Date')
    emp_dob = models.DateField('Date of Birth')
    emp_email = models.EmailField('Email Address')

class Customer(models.Model):
    cust_id = models.CharField('Customer ID', max_length = 3)
    cust_name = models.CharField('Customer Name', max_length = 50)
    cust_email = models.EmailField('Email Address')
    cust_dob = models.DateField("Customer's Date of Birth")
    