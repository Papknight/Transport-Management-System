"""TMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Monitoring import views as monit_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', monit_views.IndexView.as_view(), name="index"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('order/', monit_views.OrderView.as_view(), name="order"),
    path('today_tomorrow_view/', monit_views.TodayView.as_view(), name="today_tomorrow"),
    path('order/update/<int:pk>/', monit_views.UpdateOrderView.as_view(), name="update_order"),
    path('order/delete/<int:pk>/', monit_views.DeleteOrderView.as_view(), name="delete_order"),
    path('transports/', monit_views.TransportView.as_view(), name="transport"),
    path('portfolio/', monit_views.PortfolioView.as_view(), name="portfolio")
]
