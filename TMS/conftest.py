import pytest
from django.test import Client
from Monitoring.models import Order


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def product():
    return Order.objects.create(
        supplier='Fagor Ederlan',
        pallet=20,
        weight=2200,
        date="2021-07-05",
        hour="19:30",
        plate="DW234151",
        user="JAS"
    )
