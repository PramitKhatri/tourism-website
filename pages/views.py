from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Place,Category
from . forms import *
from django.contrib import messages

# Create your views here.


def index(request):
    return HttpResponse('this is from the products app')

# to fetch all data from the database
def showplaces(request):
    places=Place.objects.all()
    context={
        'places':places
    }
    return render(request,'pages/places.html',context)

# to show add category form and post category
def addcategory(request):
    # data processing
    if request.method=='POST':
        form=CategoryForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added')
            return redirect('/pages/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'failed to add category')
            return render(request,'pages/addcategory.html',{'forms':form})


    context={
        'forms':CategoryForm
    }
    # to load addcategory form
    return render(request,'pages/addcategory.html', context)

# add product
def postplace(request):
    if request.method=='POST':
        form=PlaceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'place added')
            return redirect('/pages/addplaces')
        else:
            messages.add_message(request,messages.ERROR,'failed to add place')
            return render(request,'pages/addplace.html',{'forms':form})
    
    context={
        'forms':PlaceForm
    }
    return render(request,'pages/addplace.html',context)

#show allcategory
def showcategory(request):
    category=Category.objects.all()

    context={
        'categories':category
    }
    return render(request,'pages/allcategory.html',context)

# delete category
def deletecategory(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'category deleted')
    return redirect('/pages/allcategory')

# update category
def updatecategory(request,category_id):
    instance=Category.objects.get(id=category_id)

    if request.method =='POST':
        form = CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category updated')
            return redirect('/pages/allcategory')
        else:
            messages.add_message(request,messages.ERROR,'category updated')
            return render(request,'pages/updatecategory.html',{'forms':form})
            
    
        

    context={
        'forms':CategoryForm(instance=instance)
    }
    return render(request,'pages/updatecategory.html',context)

# delete place
def deleteplace(request,place_id):
    places=Place.objects.get(id=place_id)
    places.delete()
    messages.add_message(request,messages.SUCCESS,'place deleted')
    return redirect('/pages/allplaces')

# update product
def updateplace(request,place_id):
    instance=Place.objects.get(id=place_id)

    if request.method =='POST':
        form = PlaceForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'place updated')
            return redirect('/pages/allplaces')
        else:
            messages.add_message(request,messages.ERROR,'place updated')
            return render(request,'pages/updateplace.html',{'forms':form})
            
    
        

    context={
        'forms':PlaceForm(instance=instance)
    }
    return render(request,'pages/updateplace.html',context)
