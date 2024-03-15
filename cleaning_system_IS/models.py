from django.db import models

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Billing(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    services = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Billing for {self.customer.name}"


class BillingDetails(models.Model):
    SERVICES_CHOICES = [
        ('Basic House Cleaning', 'Basic House Cleaning'),
        ('Deep Cleaning', 'Deep Cleaning'),
        ('Spring Cleaning', 'Spring Cleaning'),
        ('Laundry Services', 'Laundry Services'),
    ]

    services = models.CharField(max_length=20, choices=SERVICES_CHOICES)
    date = models.DateField()
    time = models.TimeField()

class Order(models.Model):
    service1 = models.CharField(max_length=100)
    service2 = models.CharField(max_length=100, blank=True)
    service3 = models.CharField(max_length=100, blank=True)
    CustomerName = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"