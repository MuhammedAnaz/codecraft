from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index),
    path('portfoliodetails', views.portfoliodetails),
    path('about', views.about),
    path('logn',views.userlogin),
    path('services',views.services),
    path('portfolio',views.portfolio),
    path('team',views.team),
    path('contactpage',views.contactpage),
    path('registration',views.registration),
    path('register',views.register),
    path('log',views.log),
    path('events',views.events),
    path('userlogout',views.userlogout),
    path('eventsform',views.eventsform),
    path('events_data_store',views.events_data_store),
    path('bookingdetails',views.bookingdetails),
    path('contact',views.contact),
    path('adminlogin',views.adminlogin),
    path('adminlogin_view',views.adminlogin_view),
    path('admindashboard',views.admindashboard),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),
    path('deletebookingpage',views.deletebookingpage),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('admin_logout',views.admin_logout),
    path('contactdetails',views.contactdetails),
    path('edit_contact/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
    path('Registrationdetails',views.Registrationdetails),
    path('edit_registration/<int:reg_id>/', views.edit_registration, name='edit_registration'),
    path('delete_registration/<int:id>/',views.delete_registration, name='delete_registration')



]



    
 
