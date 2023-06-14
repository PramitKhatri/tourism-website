from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.

def show_location(request):
    getlocationdata=Location.objects.all()
    context={
        'location_inf':getlocationdata
    }
    return render(request, 'location_data/location.html',context)


def show_province_data(request,province_name):
    province_inf=Location.objects.filter(district__province__exact=province_name)
    context={
        'province_inf':province_inf
    }
    return render(request,'location_data/province.html',context)