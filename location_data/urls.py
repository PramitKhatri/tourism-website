from django.urls import path
from .views import *

urlpatterns=[
    path('location/',show_location),
    path('province/<str:province_name>',show_province_data,name='show_province_data'),
    path('addlocation/',add_location),
    path('adddistrict/',add_district),
    path('updatedistrict/<int:district_id>/<str:getprovince_name>/',updatedistrict),
    path('deletedistrict/<int:district_id>/<str:getprovince_name>/',deletedistrict),

]