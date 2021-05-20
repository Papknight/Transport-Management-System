from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import OrderForm
from .models import Order
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import ListView, FormView, RedirectView
from django.urls import reverse_lazy, reverse
from .forms import UserLoginForm
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Min, Sum, F

# Create your views here.

now = datetime.now()


class IndexView(View):
    """View shows webapp main page"""
    def get(self, request):
        return render(request, "Monitoring/index.html",)


class OrderView(View):
    """View shows form to add new delivery order and delivery schedule for the next day"""
    def get(self, request):
        user = request.user
        form = OrderForm
        today = date.today()
        tomorrow = date.today() + timedelta(days=1)
        six_tomorrow = Order.objects.filter(date=tomorrow, hour="6:00")
        six_half_tomorrow = Order.objects.filter(date=tomorrow, hour="6:30")
        seven_tomorrow = Order.objects.filter(date=tomorrow, hour="7:00")
        seven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="7:30")
        eight_tomorrow = Order.objects.filter(date=tomorrow, hour="8:00")
        eight_half_tomorrow = Order.objects.filter(date=tomorrow, hour="8:30")
        nine_tomorrow = Order.objects.filter(date=tomorrow, hour="9:00")
        nine_half_tomorrow = Order.objects.filter(date=tomorrow, hour="9:30")
        ten_tomorrow = Order.objects.filter(date=tomorrow, hour="10:00")
        ten_half_tomorrow = Order.objects.filter(date=tomorrow, hour="10:30")
        eleven_tomorrow = Order.objects.filter(date=tomorrow, hour="11:00")
        eleven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="11:30")
        twelve_tomorrow = Order.objects.filter(date=tomorrow, hour="12:00")
        twelve_half_tomorrow = Order.objects.filter(date=tomorrow, hour="12:30")
        thirteen_tomorrow = Order.objects.filter(date=tomorrow, hour="13:00")
        thirteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="13:30")
        fourteen_tomorrow = Order.objects.filter(date=tomorrow, hour="14:00")
        fourteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="14:30")
        fifteen_tomorrow = Order.objects.filter(date=tomorrow, hour="15:00")
        fifteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="15:30")
        sixteen_tomorrow = Order.objects.filter(date=tomorrow, hour="16:00")
        sixteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="16:30")
        seventeen_tomorrow = Order.objects.filter(date=tomorrow, hour="17:00")
        seventeen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="17:30")
        eighteen_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")
        eighteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")
        nineteen_tomorrow = Order.objects.filter(date=tomorrow, hour="19:00")
        nineteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="19:30")
        twenty_tomorrow = Order.objects.filter(date=tomorrow, hour="20:00")
        twenty_half_tomorrow = Order.objects.filter(date=tomorrow, hour="20:30")
        twenty_one_tomorrow = Order.objects.filter(date=tomorrow, hour="21:00")
        twenty_one_half_tomorrow = Order.objects.filter(date=tomorrow, hour="21:30")

        context = {
            "form": form,
            "new": True,
            "today": today,
            "tomorrow": tomorrow,
            "six_tomorrow": six_tomorrow,
            "six_half_tomorrow": six_half_tomorrow,
            "seven_tomorrow": seven_tomorrow,
            "seven_half_tomorrow": seven_half_tomorrow,
            "eight_tomorrow": eight_tomorrow,
            "eight_half_tomorrow": eight_half_tomorrow,
            "nine_tomorrow": nine_tomorrow,
            "nine_half_tomorrow": nine_half_tomorrow,
            "ten_tomorrow": ten_tomorrow,
            "ten_half_tomorrow": ten_half_tomorrow,
            "eleven_tomorrow": eleven_tomorrow,
            "eleven_half_tomorrow": eleven_half_tomorrow,
            "twelve_tomorrow": twelve_tomorrow,
            "twelve_half_tomorrow": twelve_half_tomorrow,
            "thirteen_tomorrow": thirteen_tomorrow,
            "thirteen_half_tomorrow": thirteen_half_tomorrow,
            "fourteen_tomorrow": fourteen_tomorrow,
            "fourteen_half_tomorrow": fourteen_half_tomorrow,
            "fifteen_tomorrow": fifteen_tomorrow,
            "fifteen_half_tomorrow": fifteen_half_tomorrow,
            "sixteen_tomorrow": sixteen_tomorrow,
            "sixteen_half_tomorrow": sixteen_half_tomorrow,
            "seventeen_tomorrow": seventeen_tomorrow,
            "seventeen_half_tomorrow": seventeen_half_tomorrow,
            "eighteen_tomorrow": eighteen_tomorrow,
            "eighteen_half_tomorrow": eighteen_half_tomorrow,
            "nineteen_tomorrow": nineteen_tomorrow,
            "nineteen_half_tomorrow": nineteen_half_tomorrow,
            "twenty_tomorrow": twenty_tomorrow,
            "twenty_half_tomorrow": twenty_half_tomorrow,
            "twenty_one_tomorrow": twenty_one_tomorrow,
            "twenty_one_half_tomorrow": twenty_one_half_tomorrow,
            "user": user,
        }
        return render(request, 'Monitoring/order_form.html', context)

    def post(self, request):
        """
        Add to database new delivery order
        Checking if window slot is available
        If yes, add record and shows successful message
        If no, refresh page and shows information about not available slot window
        """
        user = request.user
        form = OrderForm(request.POST)
        if not form.is_valid():
            return redirect('Monitoring/index.html')
        else:
            try:
                obj = Order()
                obj.supplier = form.cleaned_data["supplier"]
                obj.pallet = form.cleaned_data["pallet"]
                obj.weight = form.cleaned_data["weight"]
                obj.date = form.cleaned_data["date"]
                obj.hour = form.cleaned_data["hour"]
                obj.plate = form.cleaned_data["plate"]
                obj.user = user
                if len(Order.objects.filter(date=obj.date, hour=obj.hour)) == 1:
                    messages.error(request, 'Window slot is not available')
                    messages.error(request, form.errors)
                    form = OrderForm()
                    user = request.user
                    form = OrderForm
                    today = date.today()
                    tomorrow = date.today() + timedelta(days=1)
                    six_tomorrow = Order.objects.filter(date=tomorrow, hour="6:00")
                    six_half_tomorrow = Order.objects.filter(date=tomorrow, hour="6:30")
                    seven_tomorrow = Order.objects.filter(date=tomorrow, hour="7:00")
                    seven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="7:30")
                    eight_tomorrow = Order.objects.filter(date=tomorrow, hour="8:00")
                    eight_half_tomorrow = Order.objects.filter(date=tomorrow, hour="8:30")
                    nine_tomorrow = Order.objects.filter(date=tomorrow, hour="9:00")
                    nine_half_tomorrow = Order.objects.filter(date=tomorrow, hour="9:30")
                    ten_tomorrow = Order.objects.filter(date=tomorrow, hour="10:00")
                    ten_half_tomorrow = Order.objects.filter(date=tomorrow, hour="10:30")
                    eleven_tomorrow = Order.objects.filter(date=tomorrow, hour="11:00")
                    eleven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="11:30")
                    twelve_tomorrow = Order.objects.filter(date=tomorrow, hour="12:00")
                    twelve_half_tomorrow = Order.objects.filter(date=tomorrow, hour="12:30")
                    thirteen_tomorrow = Order.objects.filter(date=tomorrow, hour="13:00")
                    thirteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="13:30")
                    fourteen_tomorrow = Order.objects.filter(date=tomorrow, hour="14:00")
                    fourteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="14:30")
                    fifteen_tomorrow = Order.objects.filter(date=tomorrow, hour="15:00")
                    fifteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="15:30")
                    sixteen_tomorrow = Order.objects.filter(date=tomorrow, hour="16:00")
                    sixteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="16:30")
                    seventeen_tomorrow = Order.objects.filter(date=tomorrow, hour="17:00")
                    seventeen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="17:30")
                    eighteen_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")
                    eighteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")
                    nineteen_tomorrow = Order.objects.filter(date=tomorrow, hour="19:00")
                    nineteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="19:30")
                    twenty_tomorrow = Order.objects.filter(date=tomorrow, hour="20:00")
                    twenty_half_tomorrow = Order.objects.filter(date=tomorrow, hour="20:30")
                    twenty_one_tomorrow = Order.objects.filter(date=tomorrow, hour="21:00")
                    twenty_one_half_tomorrow = Order.objects.filter(date=tomorrow, hour="21:30")

                    context = {
                        "form": form,
                        "new": True,
                        "today": today,
                        "tomorrow": tomorrow,
                        "six_tomorrow": six_tomorrow,
                        "six_half_tomorrow": six_half_tomorrow,
                        "seven_tomorrow": seven_tomorrow,
                        "seven_half_tomorrow": seven_half_tomorrow,
                        "eight_tomorrow": eight_tomorrow,
                        "eight_half_tomorrow": eight_half_tomorrow,
                        "nine_tomorrow": nine_tomorrow,
                        "nine_half_tomorrow": nine_half_tomorrow,
                        "ten_tomorrow": ten_tomorrow,
                        "ten_half_tomorrow": ten_half_tomorrow,
                        "eleven_tomorrow": eleven_tomorrow,
                        "eleven_half_tomorrow": eleven_half_tomorrow,
                        "twelve_tomorrow": twelve_tomorrow,
                        "twelve_half_tomorrow": twelve_half_tomorrow,
                        "thirteen_tomorrow": thirteen_tomorrow,
                        "thirteen_half_tomorrow": thirteen_half_tomorrow,
                        "fourteen_tomorrow": fourteen_tomorrow,
                        "fourteen_half_tomorrow": fourteen_half_tomorrow,
                        "fifteen_tomorrow": fifteen_tomorrow,
                        "fifteen_half_tomorrow": fifteen_half_tomorrow,
                        "sixteen_tomorrow": sixteen_tomorrow,
                        "sixteen_half_tomorrow": sixteen_half_tomorrow,
                        "seventeen_tomorrow": seventeen_tomorrow,
                        "seventeen_half_tomorrow": seventeen_half_tomorrow,
                        "eighteen_tomorrow": eighteen_tomorrow,
                        "eighteen_half_tomorrow": eighteen_half_tomorrow,
                        "nineteen_tomorrow": nineteen_tomorrow,
                        "nineteen_half_tomorrow": nineteen_half_tomorrow,
                        "twenty_tomorrow": twenty_tomorrow,
                        "twenty_half_tomorrow": twenty_half_tomorrow,
                        "twenty_one_tomorrow": twenty_one_tomorrow,
                        "twenty_one_half_tomorrow": twenty_one_half_tomorrow,
                        "user": user,
                    }
                    return render(request, 'Monitoring/order_form.html', context)
                # obj.user = form.cleaned_data[user.id]
                obj.save()
            except Exception as e:
                ctx = {'error': e}
                return render(request, 'registration/login.html', ctx)
        messages.success(request, 'Delivery order submitted successfully.')
        form = OrderForm()
        user = request.user
        form = OrderForm
        today = date.today()
        tomorrow = date.today() + timedelta(days=1)
        six_tomorrow = Order.objects.filter(date=tomorrow, hour="6:00")
        six_half_tomorrow = Order.objects.filter(date=tomorrow, hour="6:30")
        seven_tomorrow = Order.objects.filter(date=tomorrow, hour="7:00")
        seven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="7:30")
        eight_tomorrow = Order.objects.filter(date=tomorrow, hour="8:00")
        eight_half_tomorrow = Order.objects.filter(date=tomorrow, hour="8:30")
        nine_tomorrow = Order.objects.filter(date=tomorrow, hour="9:00")
        nine_half_tomorrow = Order.objects.filter(date=tomorrow, hour="9:30")
        ten_tomorrow = Order.objects.filter(date=tomorrow, hour="10:00")
        ten_half_tomorrow = Order.objects.filter(date=tomorrow, hour="10:30")
        eleven_tomorrow = Order.objects.filter(date=tomorrow, hour="11:00")
        eleven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="11:30")
        twelve_tomorrow = Order.objects.filter(date=tomorrow, hour="12:00")
        twelve_half_tomorrow = Order.objects.filter(date=tomorrow, hour="12:30")
        thirteen_tomorrow = Order.objects.filter(date=tomorrow, hour="13:00")
        thirteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="13:30")
        fourteen_tomorrow = Order.objects.filter(date=tomorrow, hour="14:00")
        fourteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="14:30")
        fifteen_tomorrow = Order.objects.filter(date=tomorrow, hour="15:00")
        fifteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="15:30")
        sixteen_tomorrow = Order.objects.filter(date=tomorrow, hour="16:00")
        sixteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="16:30")
        seventeen_tomorrow = Order.objects.filter(date=tomorrow, hour="17:00")
        seventeen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="17:30")
        eighteen_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")
        eighteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")
        nineteen_tomorrow = Order.objects.filter(date=tomorrow, hour="19:00")
        nineteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="19:30")
        twenty_tomorrow = Order.objects.filter(date=tomorrow, hour="20:00")
        twenty_half_tomorrow = Order.objects.filter(date=tomorrow, hour="20:30")
        twenty_one_tomorrow = Order.objects.filter(date=tomorrow, hour="21:00")
        twenty_one_half_tomorrow = Order.objects.filter(date=tomorrow, hour="21:30")

        context = {
            "form": form,
            "new": True,
            "today": today,
            "tomorrow": tomorrow,
            "six_tomorrow": six_tomorrow,
            "six_half_tomorrow": six_half_tomorrow,
            "seven_tomorrow": seven_tomorrow,
            "seven_half_tomorrow": seven_half_tomorrow,
            "eight_tomorrow": eight_tomorrow,
            "eight_half_tomorrow": eight_half_tomorrow,
            "nine_tomorrow": nine_tomorrow,
            "nine_half_tomorrow": nine_half_tomorrow,
            "ten_tomorrow": ten_tomorrow,
            "ten_half_tomorrow": ten_half_tomorrow,
            "eleven_tomorrow": eleven_tomorrow,
            "eleven_half_tomorrow": eleven_half_tomorrow,
            "twelve_tomorrow": twelve_tomorrow,
            "twelve_half_tomorrow": twelve_half_tomorrow,
            "thirteen_tomorrow": thirteen_tomorrow,
            "thirteen_half_tomorrow": thirteen_half_tomorrow,
            "fourteen_tomorrow": fourteen_tomorrow,
            "fourteen_half_tomorrow": fourteen_half_tomorrow,
            "fifteen_tomorrow": fifteen_tomorrow,
            "fifteen_half_tomorrow": fifteen_half_tomorrow,
            "sixteen_tomorrow": sixteen_tomorrow,
            "sixteen_half_tomorrow": sixteen_half_tomorrow,
            "seventeen_tomorrow": seventeen_tomorrow,
            "seventeen_half_tomorrow": seventeen_half_tomorrow,
            "eighteen_tomorrow": eighteen_tomorrow,
            "eighteen_half_tomorrow": eighteen_half_tomorrow,
            "nineteen_tomorrow": nineteen_tomorrow,
            "nineteen_half_tomorrow": nineteen_half_tomorrow,
            "twenty_tomorrow": twenty_tomorrow,
            "twenty_half_tomorrow": twenty_half_tomorrow,
            "twenty_one_tomorrow": twenty_one_tomorrow,
            "twenty_one_half_tomorrow": twenty_one_half_tomorrow,
            "user": user,
        }

        return render(request, 'Monitoring/order_form.html', context)


class TodayView(View):
    """
    Only for superusers
    Shows info about deliveries for today and tomorrow
    """
    def get(self, request):
        today = date.today()
        tomorrow = date.today() + timedelta(days=1)

        six = Order.objects.filter(date=today, hour="6:00")
        six_tomorrow = Order.objects.filter(date=tomorrow, hour="6:00")

        six_half = Order.objects.filter(date=today, hour="6:30")
        six_half_tomorrow = Order.objects.filter(date=tomorrow, hour="6:30")

        seven = Order.objects.filter(date=today, hour="7:00")
        seven_tomorrow = Order.objects.filter(date=tomorrow, hour="7:00")

        seven_half = Order.objects.filter(date=today, hour="7:30")
        seven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="7:30")

        eight = Order.objects.filter(date=today, hour="8:00")
        eight_tomorrow = Order.objects.filter(date=tomorrow, hour="8:00")

        eight_half = Order.objects.filter(date=today, hour="8:30")
        eight_half_tomorrow = Order.objects.filter(date=tomorrow, hour="8:30")

        nine = Order.objects.filter(date=today, hour="9:00")
        nine_tomorrow = Order.objects.filter(date=tomorrow, hour="9:00")

        nine_half = Order.objects.filter(date=today, hour="9:30")
        nine_half_tomorrow = Order.objects.filter(date=tomorrow, hour="9:30")

        ten = Order.objects.filter(date=today, hour="10:00")
        ten_tomorrow = Order.objects.filter(date=tomorrow, hour="10:00")

        ten_half = Order.objects.filter(date=today, hour="10:30")
        ten_half_tomorrow = Order.objects.filter(date=tomorrow, hour="10:30")

        eleven = Order.objects.filter(date=today, hour="11:00")
        eleven_tomorrow = Order.objects.filter(date=tomorrow, hour="11:00")

        eleven_half = Order.objects.filter(date=today, hour="11:30")
        eleven_half_tomorrow = Order.objects.filter(date=tomorrow, hour="11:30")

        twelve = Order.objects.filter(date=today, hour="12:00")
        twelve_tomorrow = Order.objects.filter(date=tomorrow, hour="12:00")

        twelve_half = Order.objects.filter(date=today, hour="12:30")
        twelve_half_tomorrow = Order.objects.filter(date=tomorrow, hour="12:30")

        thirteen = Order.objects.filter(date=today, hour="13:00")
        thirteen_tomorrow = Order.objects.filter(date=tomorrow, hour="13:00")

        thirteen_half = Order.objects.filter(date=today, hour="13:30")
        thirteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="13:30")

        fourteen = Order.objects.filter(date=today, hour="14:00")
        fourteen_tomorrow = Order.objects.filter(date=tomorrow, hour="14:00")

        fourteen_half = Order.objects.filter(date=today, hour="14:30")
        fourteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="14:30")

        fifteen = Order.objects.filter(date=today, hour="15:00")
        fifteen_tomorrow = Order.objects.filter(date=tomorrow, hour="15:00")

        fifteen_half = Order.objects.filter(date=today, hour="15:30")
        fifteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="15:30")

        sixteen = Order.objects.filter(date=today, hour="16:00")
        sixteen_tomorrow = Order.objects.filter(date=tomorrow, hour="16:00")

        sixteen_half = Order.objects.filter(date=today, hour="16:30")
        sixteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="16:30")

        seventeen = Order.objects.filter(date=today, hour="17:00")
        seventeen_tomorrow = Order.objects.filter(date=tomorrow, hour="17:00")

        seventeen_half = Order.objects.filter(date=today, hour="17:30")
        seventeen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="17:30")

        eighteen = Order.objects.filter(date=today, hour="18:00")
        eighteen_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")

        eighteen_half = Order.objects.filter(date=today, hour="18:30")
        eighteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="18:30")

        nineteen = Order.objects.filter(date=today, hour="19:00")
        nineteen_tomorrow = Order.objects.filter(date=tomorrow, hour="19:00")

        nineteen_half = Order.objects.filter(date=today, hour="19:30")
        nineteen_half_tomorrow = Order.objects.filter(date=tomorrow, hour="19:30")

        twenty = Order.objects.filter(date=today, hour="20:00")
        twenty_tomorrow = Order.objects.filter(date=tomorrow, hour="20:00")

        twenty_half = Order.objects.filter(date=today, hour="20:30")
        twenty_half_tomorrow = Order.objects.filter(date=tomorrow, hour="20:30")

        twenty_one = Order.objects.filter(date=today, hour="21:00")
        twenty_one_tomorrow = Order.objects.filter(date=tomorrow, hour="21:00")

        twenty_one_half = Order.objects.filter(date=today, hour="21:30")
        twenty_one_half_tomorrow = Order.objects.filter(date=tomorrow, hour="21:30")

        user = request.user

        context = {
            "today": today,
            "tomorrow": tomorrow,
            "six": six,
            "six_tomorrow": six_tomorrow,
            "six_half": six_half,
            "six_half_tomorrow": six_half_tomorrow,
            "seven": seven,
            "seven_tomorrow": seven_tomorrow,
            "seven_half": seven_half,
            "seven_half_tomorrow": seven_half_tomorrow,
            "eight": eight,
            "eight_tomorrow": eight_tomorrow,
            "eight_half": eight_half,
            "eight_half_tomorrow": eight_half_tomorrow,
            "nine": nine,
            "nine_tomorrow": nine_tomorrow,
            "nine_half": nine_half,
            "nine_half_tomorrow": nine_half_tomorrow,
            "ten": ten,
            "ten_tomorrow": ten_tomorrow,
            "ten_half": ten_half,
            "ten_half_tomorrow": ten_half_tomorrow,
            "eleven": eleven,
            "eleven_tomorrow": eleven_tomorrow,
            "eleven_half": eleven_half,
            "eleven_half_tomorrow": eleven_half_tomorrow,
            "twelve": twelve,
            "twelve_tomorrow": twelve_tomorrow,
            "twelve_half": twelve_half,
            "twelve_half_tomorrow": twelve_half_tomorrow,
            "thirteen": thirteen,
            "thirteen_tomorrow": thirteen_tomorrow,
            "thirteen_half": thirteen_half,
            "thirteen_half_tomorrow": thirteen_half_tomorrow,
            "fourteen": fourteen,
            "fourteen_tomorrow": fourteen_tomorrow,
            "fourteen_half": fourteen_half,
            "fourteen_half_tomorrow": fourteen_half_tomorrow,
            "fifteen": fifteen,
            "fifteen_tomorrow": fifteen_tomorrow,
            "fifteen_half": fifteen_half,
            "fifteen_half_tomorrow": fifteen_half_tomorrow,
            "sixteen": sixteen,
            "sixteen_tomorrow": sixteen_tomorrow,
            "sixteen_half": sixteen_half,
            "sixteen_half_tomorrow": sixteen_half_tomorrow,
            "seventeen": seventeen,
            "seventeen_tomorrow": seventeen_tomorrow,
            "seventeen_half": seventeen_half,
            "seventeen_half_tomorrow": seventeen_half_tomorrow,
            "eighteen": eighteen,
            "eighteen_tomorrow": eighteen_tomorrow,
            "eighteen_half": eighteen_half,
            "eighteen_half_tomorrow": eighteen_half_tomorrow,
            "nineteen": nineteen,
            "nineteen_tomorrow": nineteen_tomorrow,
            "nineteen_half": nineteen_half,
            "nineteen_half_tomorrow": nineteen_half_tomorrow,
            "twenty": twenty,
            "twenty_tomorrow": twenty_tomorrow,
            "twenty_half": twenty_half,
            "twenty_half_tomorrow": twenty_half_tomorrow,
            "twenty_one": twenty_one,
            "twenty_one_tomorrow": twenty_one_tomorrow,
            "twenty_one_half": twenty_one_half,
            "twenty_one_half_tomorrow": twenty_one_half_tomorrow,
            "user": user
        }
        return render(request, "Monitoring/today_tomorrow.html", context)


class UpdateOrderView(UpdateView):
    """
    View for update existing in database delivery order
    """
    model = Order
    form_class = OrderForm
    pk_url_kwarg = 'pk'
    # orders = Order.objects.get(id=1)
    template_name = 'Monitoring/order_form.html'
    success_url = '/order'


class DeleteOrderView(DeleteView):
    """
    Delete delivery order from database
    """
    model = Order
    pk_url_kwarg = 'pk'
    template_name = 'Monitoring/delete_order.html'
    success_url = '/order'


class TransportView(View):
    """
    Only for freight forwarders
    Shows all forwarder delivery orders since today
    """
    def get(self, request):
        now = datetime.now()
        today = now.strftime("%B %d, %Y")
        orders = Order.objects.filter(date__gte=date.today()).order_by("date", "hour")
        context = {
            "orders": orders,
            "today": today,
        }
        return render(request, "Monitoring/transports.html", context)


class PortfolioView(View):
    """
    Most important thing about company
    """
    def get(self, request):
        orders = Order.objects.all()
        forwarders = Order.objects.values("user").annotate(Count("id"))
        users = User.objects.all().count() - 1
        suppliers = Order.objects.values("supplier").annotate(Count("id"))
        countries = Order.objects.all()
        context = {
            "orders": orders,
            "forwarders": forwarders,
            "users": users,
            "suppliers": suppliers,
            "countries": countries
        }
        return render(request, "Monitoring/portfolio.html", context)