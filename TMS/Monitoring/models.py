from django.db import models
from django import forms

# Create your models here.


class Region(models.Model):

    CONTINENT = {
        (0, "Europe"),
        (1, "North America"),
        (2, "South America"),
        (3, "Africa"),
        (4, "Asia"),
        (5, "Oceania"),
        (6, "Antarctica"),
        (7, "Unspecified")
    }
    short_country = models.CharField(max_length=4, blank=False)
    continent = models.PositiveIntegerField(default=7, choices=CONTINENT)

    def __str__(self):
        return self.short_country


class Country(models.Model):
    name = models.CharField(max_length=64, blank=False)
    region = models.OneToOneField(Region, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=128, blank=False)
    address = models.CharField(max_length=128, blank=False)
    city = models.CharField(max_length=128, blank=False)
    zipcode = models.CharField(max_length=40, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SupplierContact(models.Model):
    name = models.CharField(max_length=128, blank=False)
    lastname = models.CharField(max_length=128, blank=False)
    email = models.CharField(max_length=128, blank=False)
    phone = models.CharField(max_length=128, null=True, blank=True)
    mobile = models.CharField(max_length=128, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Order(models.Model):
    HOUR = {
        ("6:00", "6:00"),
        ("6:30", "6:30"),
        ("7:00", "7:00"),
        ("7:30", "7:30"),
        ("8:00", "8:00"),
        ("8:30", "8:30"),
        ("9:00", "9:00"),
        ("9:30", "9:30"),
        ("10:00", "10:00"),
        ("10:30", "10:30"),
        ("11:00", "11:00"),
        ("11:30", "11:30"),
        ("12:00", "12:00"),
        ("12:30", "12:30"),
        ("13:00", "13:00"),
        ("13:30", "13:30"),
        ("14:00", "14:00"),
        ("14:30", "14:30"),
        ("15:00", "15:00"),
        ("15:30", "15:30"),
        ("16:00", "16:00"),
        ("16:30", "16:30"),
        ("17:00", "17:00"),
        ("17:30", "17:30"),
        ("18:00", "18:00"),
        ("18:30", "18:30"),
        ("19:00", "19:00"),
        ("19:30", "19:30"),
        ("20:00", "20:00"),
        ("20:30", "20:30"),
        ("21:00", "21:00"),
        ("21:30", "21:30"),
    }
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False)
    pallet = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    date = models.DateField()
    hour = models.CharField(max_length=32, default="6:00", choices=HOUR)
    plate = models.CharField(max_length=32)
