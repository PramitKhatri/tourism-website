# Generated by Django 4.2.1 on 2023-06-13 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location_data', '0002_district_district_images_location_location_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='location_data.events'),
        ),
    ]
