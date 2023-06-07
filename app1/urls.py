from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index),
    path('portfoliodetails', views.portfoliodetails),
    path('about', views.about),
    path('logn',views.login),
    path('services',views.services),
    path('portfolio',views.portfolio),
    path('team',views.team),
    path('contactpage',views.contactpage),
    path('registration',views.registration),
    path('register',views.register),
    path('log',views.log),
    path('events',views.events),
    path('eventsform',views.eventsform),
    path('events_data_store',views.events_data_store),
    path('bookingdetails',views.bookingdetails),
    path('contact',views.contact),
    path('adminlogin',views.adminlogin),
    path('adminlogin_view',views.adminlogin_view)

]

    
 
