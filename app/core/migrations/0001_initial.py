# Generated by Django 4.2.13 on 2024-05-24 14:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('language', models.CharField(choices=[('ENGLISH', 'English'), ('GERMAN', 'German'), ('SPANISH', 'Spanish')], default='ENGLISH', max_length=100)),
                ('currency', models.CharField(choices=[('US_DOLLAR', 'US Dollar'), ('EURO', 'Euro'), ('MEXICAN_PESO', 'Mexican Peso')], default='EURO', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.provider')),
            ],
        ),
    ]
