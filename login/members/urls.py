from django.urls import path
from . import views

urlpatterns=[
    path('', views.myfirst, name='myfirst'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('departments', views.departments, name='departments'),
    path('doctors', views.doctors, name='doctors'),
]