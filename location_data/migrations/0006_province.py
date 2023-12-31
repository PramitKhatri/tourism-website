# Generated by Django 4.2.1 on 2023-06-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_data', '0005_delete_locationimagemodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=100)),
                ('province_images', models.FileField(upload_to='static/uploads/province')),
            ],
        ),
    ]
