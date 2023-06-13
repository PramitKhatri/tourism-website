# Generated by Django 4.2.1 on 2023-06-11 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('place_description', models.TextField()),
                ('place_image', models.FileField(null=True, upload_to='static/uploads')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
            ],
        ),
    ]
