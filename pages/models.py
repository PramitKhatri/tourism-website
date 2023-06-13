from django.db import models

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=100, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    category_image=models.FileField(upload_to='static/uploads',null=True)


    def __str__(self):
        return self.category_name

class Place(models.Model):
    place_name=models.CharField(max_length=100)
    place_description=models.TextField()
    place_image=models.FileField(upload_to='static/uploads',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Category=models.ForeignKey(Category,on_delete= models.CASCADE,null=True)

    def __str__(self):
        return self.place_name 

