from django.db import models

# Create your models here.
Province=(
    ("Sudurpaschim","Sudurpaschim"),
    ("Karnali Province","Karnali Province"),
    ("Lumbini Province","Lumbini Province"),
    ("Gandaki Province","Gandaki Province"),
    ("Bagmati Province","Bagmati Province"),
    ("Madesh Province","Madesh Province"),
    ("Province 1","Province 1"),
)

class District(models.Model):
    province=models.CharField(max_length=100,choices=Province)
    district_name=models.CharField(max_length=100)
    district_desc=models.TextField()
    district_images = models.ManyToManyField('DistrictImageModel', related_name='districts')

    def __str__(self):
        return self.district_name

#thss is to be able to input multiple images
class DistrictImageModel(models.Model):
    image = models.FileField(upload_to='static/uploads')

class Events(models.Model):
    event_name=models.CharField(max_length=100)
    event_desc=models.TextField()
    event_image=models.FileField(upload_to='static/uploads/events',null=True)
    event_date=models.DateField()

    def __str__(self):
        return self.event_name


class Location(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    location_name=models.CharField(max_length=100)
    location_desc=models.TextField()
    location_images = models.ManyToManyField('LocationImageModel', related_name='locations')
    best_season = models.CharField(max_length=10, default='any', choices=(('any', 'any'), ('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autumn'), ('winter', 'winter')))
    event=models.ForeignKey(Events, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.location_name
    


class LocationImageModel(models.Model):
    image = models.FileField(upload_to='static/uploads/location')

