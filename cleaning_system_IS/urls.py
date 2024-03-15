from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('welcome/', views.welcome, name='welcome'),
    path('paybill/', views.paybill, name='paybill'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('logout/', views.logout, name='logout'),
    path('success/', views.success, name='success'),
    path('view_bills/', views.view_bills, name='view_bills'),
    path('billing_details/', views.billing_details, name='billing_details'),
    path('review_orders/', views.review_orders, name='review_orders'),
    path('place_order/', views.place_order, name='place_order'),
    ]
