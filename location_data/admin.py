from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Events)
admin.site.register(Location)
admin.site.register(LocationImageModel)
admin.site.register(DistrictImageModel)
admin.site.register(District)