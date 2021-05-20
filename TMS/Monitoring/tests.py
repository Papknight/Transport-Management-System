from django.test import TestCase
import pytest
from django.urls import reverse

from .models import Order


@pytest.mark.django_db
def test_order_modify_view(client, order):
    response = client.get(f'/order/update/{order.pk}/')
    assert response.status_code == 200
    assert response.context['supplier'] == order.supplier
    assert response.context['pallet'] == order.pallet
    assert response.context['weight'] == order.weight
    assert response.context['date'] == order.date
    assert response.context['hour'] == order.hour
    assert response.context['plate'] == order.plate
    assert response.context['user'] == order.user


@pytest.mark.django_db
def test_product_add(client):
    response = client.post(f'/order/', {'supplier': 'AHC Polska', 'pallet': 20, 'weight': 2200, 'date': '2021-07-05',
                                        'hour': "14:00", 'plate': "DW21516F", 'user': "JAS"})
    assert response.status_code == 302
    assert Order.objects.filter(date='2021-07-05', hour='14:00').count() == 1


@pytest.mark.django_db
def test_product_delete(client, order):
    response = client.post(f'/order/delete/{order.pk}/')
    assert response.status_code == 302
    assert Order.objects.filter(pk=order.pk).count() == 0


@pytest.mark.django_db
def test_transport_view(client):
    assert Order.objects.create(supplier='AHC Polska', pallet=20, weight=2200, date='2021-07-05', hour="14:00",
                                plate="DW21516F", user="JAS")
    assert Order.objects.create(supplier='Brovedani SPA', pallet=50, weight=2200, date='2021-07-05', hour="14:30",
                                plate="DW2151FFA", user="JAS")
    assert Order.objects.create(supplier='Draxton PL', pallet=50, weight=2500, date='2021-07-05', hour="15:30",
                                plate="DW21242GSA", user="JAS")
    response = client.get(f'/transports/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_monitoring_view(client):
    response = client.get(f'/transports/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_portfolio_view(client):
    response = client.get(f'/portfolio/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_unauthorized(client):
    url = reverse('superuser-url')
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_superuser_view(admin_client):
    url = reverse('superuser-url')
    response = admin_client.get(url)
    assert response.status_code == 200


