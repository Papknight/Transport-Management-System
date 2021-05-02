from django.contrib.auth import get_user_model, authenticate
from django import forms
from .models import Order

User = get_user_model()


class UserLoginForm(forms.ModelForm):
    # password1 = forms.CharField(label="Hasło")
    username = forms.CharField(label="Nazwa użytkownika")

    class Meta:
        model = User
        fields = ('password', )

    def clean(self):
        cd = super().clean()
        username = cd['username']
        password = cd['password']
        user = authenticate(username=username, password=password)

        if user is None:
            self.add_error(None, 'Podaj poprawnie dane')
        self.user = user


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'pallet', 'weight', 'date', 'hour', 'plate']
        widgets = {
            'date': forms.SelectDateWidget,
        }