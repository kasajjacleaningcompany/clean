from django.contrib import admin
from .models import Customer, Billing, BillingDetails, Order

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Billing)
admin.site.register(BillingDetails)
