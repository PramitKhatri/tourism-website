from django.urls import path
from .views import *

urlpatterns=[
    path('location/',show_location),
    path('province/<str:province_name>',show_province_data)
]