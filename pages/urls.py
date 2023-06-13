from django.urls import path
from . views import *


urlpatterns=[
     path('test/',index),
     path('allplaces/', showplaces),
     path('addcategory/', addcategory),
     path('addplaces/',postplace),
     path('allcategory/',showcategory),
     path('deletecategory/<int:category_id>',deletecategory),
     path('updatecategory/<int:category_id>',updatecategory),
     path('deleteplace/<int:place_id>',deleteplace),
     path('updateplace/<int:place_id>',updateplace)
]