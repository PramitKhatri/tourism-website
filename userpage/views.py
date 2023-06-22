from django.shortcuts import render,redirect
from location_data.models import *
from django.contrib.auth.decorators import login_required
from pages.forms import *
from django.contrib import messages

# Create your views here.


def homepage(request):
    
    context={
        'provinces':Province
    }
    return render(request,'userpage/home.html',context)

def placedetails(request,place_id):
    place=Place.objects.get(id=place_id)
    context={
        'place':place
    }
    return render(request,'userpage/placedetails.html',context)

def showplaces(request):
    places=Place.objects.all()
    context={
        'places':places 

    }

    return render (request,'userpage/places.html',context)




