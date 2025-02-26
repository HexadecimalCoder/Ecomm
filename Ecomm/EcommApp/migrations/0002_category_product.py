# Generated by Django 5.1.3 on 2024-12-04 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default=1, max_length=200, null=True)),
                ('image1', models.ImageField(upload_to='uploads/products')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/products')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='uploads/products')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='uploads/products')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='uploads/products')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EcommApp.category')),
            ],
        ),
    ]
