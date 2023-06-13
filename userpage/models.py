from django.db import models
from pages.models import Place
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)