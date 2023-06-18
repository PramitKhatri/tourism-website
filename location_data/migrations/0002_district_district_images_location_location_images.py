# Generated by Django 4.2.1 on 2023-06-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='district_images',
            field=models.ManyToManyField(related_name='districts', to='location_data.districtimagemodel'),
        ),
        migrations.AddField(
            model_name='location',
            name='location_images',
            field=models.ManyToManyField(related_name='locations', to='location_data.locationimagemodel'),
        ),
    ]