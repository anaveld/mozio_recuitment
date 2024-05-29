from django.db import models
from django.contrib.gis.db.models.fields import PolygonField
from app import constants


class Provider(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    language = models.CharField(max_length=100, choices=constants.LANGUAGE_CHOICES, default=constants.ENG)
    currency = models.CharField(max_length=100, choices=constants.CURRENCY_CHOICES, default=constants.EUR)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    area = PolygonField()

    @property
    def full_price(self):
        return '%s %s' % (self.price, self.provider.currency)
