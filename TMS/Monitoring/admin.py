from django.contrib import admin
from .models import Supplier, SupplierContact, Country, Region, Order
# Register your models here.

admin.site.register(Supplier)
admin.site.register(SupplierContact)
admin.site.register(Country)
admin.site.register(Order)