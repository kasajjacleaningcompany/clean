from django import forms
from .models import Customer, Billing, BillingDetails,Order

from django import forms
from .models import Customer

class SignupForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['name', 'password', 'confirm_password']

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['services', 'date', 'time']

from .models import BillingDetails

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = ['services', 'date', 'time']

class OrderForm(forms.Form):
    service1 = forms.CharField(max_length=100, label='Service 1')
    service2 = forms.CharField(max_length=100, label='Service 2', required=False)
    service3 = forms.CharField(max_length=100, label='Service 3', required=False)
    CustomerName = forms.CharField(max_length=100, label='Customer Name')