from django.shortcuts import render
from django.http import HttpResponse
from .models import department,doctor
from .forms import bookingform
def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cnf.html')
    form=bookingform()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)


def contact(request):
    return render(request, 'contact.html')


def doctors(request):
    dict_docs={
       'doctors': doctor.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)


def departments(request):
    dict_dep={
        'dept':department.objects.all()
    }
    return render(request, 'department.html',dict_dep)



def myfirst(request):
    
    return render(request, 'myfirst.html')







# Create your views here.
