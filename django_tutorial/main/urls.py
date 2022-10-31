from django.urls import path
from . import views # . references current directory

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name = 'sign_up'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('add_cust', views.add_customer, name = 'add_cust')
]