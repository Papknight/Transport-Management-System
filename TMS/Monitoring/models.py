from django.db import models
from django import forms
from django.contrib.auth.models import User

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


class Hour(models.TextChoices):
    six = "6:00", "6:00"
    six_half = "6:30", "6:30"
    seven = "7:00", "7:00"
    seven_half = "7:30", "7:30"
    eight = "8:00", "8:00"
    eight_half = "8:30", "8:30"
    nine = "9:00", "9:00"
    nine_half = "9:30", "9:30"
    ten = "10:00", "10:00"
    ten_half = "10:30", "10:30"
    eleven = "11:00", "11:00"
    eleven_half = "11:30", "11:30"
    twelve = "12:00", "12:00"
    twelve_half = "12:30", "12:30"
    thirteen = "13:00", "13:00"
    thirteen_half = "13:30", "13:30"
    fourteen = "14:00", "14:00"
    fourteen_half = "14:30", "14:30"
    fifteen = "15:00", "15:00"
    fifteen_half = "15:30", "15:30"
    sixteen = "16:00", "16:00"
    sixteen_half = "16:30", "16:30"
    seventeen = "17:00", "17:00"
    seventeen_half = "17:30", "17:30"
    eighteen = "18:00", "18:00"
    eighteen_half = "18:30", "18:30"
    nineteen = "19:00", "19:00"
    nineteen_half = "19:30", "19:30"
    twenty = "20:00", "20:00",
    twenty_half = "20:30", "20:30"
    twenty_one = "21:00", "21:00"
    twenty_one_half = "21:30", "21:30"


class Order(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False)
    pallet = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    date = models.DateField()
    hour = models.CharField(max_length=32, choices=Hour.choices)
    plate = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


