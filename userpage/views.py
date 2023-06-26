from django.shortcuts import render,redirect
from location_data.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def homepage(request):
    provinces=Province.objects.all()
    context={
        'provinces':provinces
    }
    return render(request,'userpage/home.html',context)



