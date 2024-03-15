from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm, LoginForm, Billing, BillingDetails,OrderForm
from .models import BillingDetails, Customer, Billing, Order

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            try:
                customer = Customer.objects.get(name=name, password=password)
                # Perform further validation or authentication if required

                # Redirect to welcome.html upon successful login
                return redirect('welcome')
            except Customer.DoesNotExist:
                # Handle invalid login
                return redirect('index')
    else:
        form = LoginForm()
    
    return render(request, 'index.html', {'form': form})

    

def logout(request):
    logout(request)
    return redirect('index')


from .forms import BillingDetailsForm

def welcome(request):
    if request.method == 'POST':
        form = BillingDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BillingDetailsForm()
    return render(request, 'welcome.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def aboutUs(request):
    return render(request, 'aboutUs.html')


from .models import Billing

def view_bills(request):
    billing_data = Billing.objects.all()
    context = {
        'billing_details': billing_data
    }
    return render(request, 'view_bills.html', context)


def paybill(request):
    return render(request, 'paybill.html')


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='admin_login')
def billing_details(request):
    if not request.user.is_staff:
        return redirect('index')
    billing_entries = Billing.objects.all()
    return render(request, 'billing_details.html', {'billing_details': billing_entries})

@staff_member_required(login_url='admin_login')
def review_orders(request):
    orders = Order.objects.all()
    return render(request, 'review_orders.html', {'orders': orders})



def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            service1 = form.cleaned_data['service1']
            service2 = form.cleaned_data['service2']
            service3 = form.cleaned_data['service3']
            CustomerName = form.cleaned_data['CustomerName']
            
            # Create an Order object and save it to the database
            order = Order(service1=service1, service2=service2, service3=service3, CustomerName=CustomerName,)
            order.save()
            
            return redirect('success')  # Redirect to the review_orders view
    else:
        form = OrderForm()
    
    return render(request, 'place_order.html', {'form': form})


from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login

@user_passes_test(lambda u: u.is_superuser)
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('billing_details')
        else:
            # Invalid credentials, handle the error as needed
            return render(request, 'index.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'index.html')