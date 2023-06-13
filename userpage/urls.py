from django.urls import path
from .views import *


urlpatterns=[
    path('',homepage),
    path('placedetails/<int:place_id>',placedetails),
    path('place/',showplaces),
    # path('category/',showcategory),

]