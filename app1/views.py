from django.shortcuts import render,redirect, get_object_or_404
from app1.models import Registration, Booking,Contact
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout





# Create your views here.

def index(request):
    return render(request, 'index.html')

def portfoliodetails(request):
    return render(request,'portfolio-details.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html') 

def portfolio(request):
    return render(request,'portfolio.html')

def team(request):
    return render(request,'team.html')
    
def contactpage(request):
    return render(request, 'contact.html')  

def userlogin(request):
    return render(request,'login.html')

def registration(request):
    return render(request, 'registration.html')

def register(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        ag=request.POST.get('age')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        ps=request.POST.get('password')
        obj=Registration(Name=nm,Age=ag,Email=em,Phone_number=ph,Password=ps)
        obj.save()
    return render(request,'login.html')

def log(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        ps = request.POST.get('password')
        try:
            user = Registration.objects.get(Email=em, Password=ps)
            request.session['user_id'] = user.id
            return render(request, 'events.html')
        except Registration.DoesNotExist:
            error_message = "Incorrect Email or Password"
            messages.error(request, error_message)
    # If the code reaches this point, either it's a GET request or the login failed
    return render(request, 'login.html')

def userlogout(request):
    Session.objects.all().delete()
    return render(request,'login.html')

def events(request):
    return render(request, 'events.html')

def eventsform(request):
    return render(request,'eventsform.html')

def events_data_store(request):
    if request.method == 'POST':
        ev = request.POST.get("event")
        pr = request.POST.get("price")
        nm = request.POST.get("name")
        ph = request.POST.get("phone")
        em = request.POST.get("email")
        np = request.POST.get("persons")
        total_price = int(pr) * int(np)
        obj = Booking(event=ev, price=pr, name=nm, phone=ph, email=em, number_of_persons=np, totalprice=total_price)
        obj.save()
        messages.success(request, 'Booking successful!')
        return render(request, 'eventsform.html')
    return render(request, 'eventsform.html')

def bookingdetails(request):
    bookings = Booking.objects.all()
    return render(request, 'bookingdetails.html', {'bookings': bookings})
def contact(request):
    if request.method == 'POST':
        na=request.POST.get("name")
        em=request.POST.get("email")
        sub=request.POST.get("subject")
        msg=request.POST.get("message")
        obj=Contact(name=na,email=em,subject=sub,message=msg)
        obj.save()
    return render(request,'contact.html')

def adminlogin(request):
    return render(request,'adminlogin.html')    



def adminlogin_view(request):
    if request.method == 'POST':
        # Retrieve username and password from the submitted form
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If authentication is successful, log in the user
            login(request, user)
            return redirect('/admindashboard')  # Redirect to the admin dashboard page
        else:
            # If authentication fails, set an error message
            error_message = 'Invalid credentials'
    else:
        # If it's not a POST request, initialize error_message as None
        error_message = None

    # Render the adminlogin.html template, passing the error_message to display in the template
    return render(request, 'adminlogin.html', {'error_message': error_message})

def admindashboard(request):
    return render(request,'admindashboard.html')
def deletebookingpage(request):
    return render(request,'delete_booking.html')

def delete_booking(request, id):
    # Retrieve the booking object based on the provided id
    booking = Booking.objects.get(pk=id)

    if request.method == 'POST':
        # If it's a POST request, delete the booking object from the database
        booking.delete()
        return redirect('/bookingdetails')  # Redirect to the booking details page

    # If it's not a POST request, render the delete_booking.html template
    # Pass the booking object to the template to display the details
    return render(request, 'delete_booking.html', {'booking': booking})


def edit_booking(request, booking_id):
    # Retrieve the booking object with the specified ID or return a 404 error
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        # Update the booking object with the new values from the form
        booking.name = request.POST.get('name')
        booking.phone = request.POST.get('phone')
        booking.email = request.POST.get('email')
        booking.event = request.POST.get('event')
        booking.number_of_persons = request.POST.get('number_of_persons')
        booking.price = request.POST.get('price')
        booking.totalprice = request.POST.get('totalprice')
        booking.save()  # Save the updated booking object to the database
        # Redirect to the booking details page for the updated booking
        return redirect('/bookingdetails', booking_id=booking.id)
    
    # Render the edit booking form template with the booking object
    return render(request, 'edit_booking.html', {'booking': booking})

def admin_logout(request):
    logout(request)
    return redirect('/adminlogin')  # Replace 'admin_login' with the appropriate URL name for your admin login page    
def contactdetails(request):
    contacts = Contact.objects.all()
    return render(request, 'contactdetails.html', {'contacts':contacts })

def edit_contact(request, contact_id):
    # Retrieve the contact object with the specified ID or return a 404 error
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        # Update the contact object with the new values from the form
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()  # Save the updated contact object to the database
        # Redirect to the contact details page for the updated contact
        return redirect('/contactdetails', contact_id=contact.id)

    # Render the edit contact form template with the contact object
    return render(request, 'editcontact.html', {'contact': contact})
def delete_contact(request, id):
    # Retrieve the booking object based on the provided id
    contact = Contact.objects.get(pk=id)
    if request.method == 'POST':
        # If it's a POST request, delete the booking object from the database
        contact.delete()
        return redirect('/contactdetails')  # Redirect to the booking details page

    # If it's not a POST request, render the delete_booking.html template
    # Pass the booking object to the template to display the details
    return render(request, 'deletecontact.html', {'contact': contact})
def Registrationdetails(request):
    reg = Registration.objects.all()
    return render(request, 'registrationdetails.html', {'reg':reg })

def edit_registration(request, reg_id):
    reg = get_object_or_404(Registration, id=reg_id)
    if request.method == 'POST':
        reg.Name = request.POST.get('name')
        reg.Age = request.POST.get('age')
        reg.Email = request.POST.get('email')
        reg.Phone_number = request.POST.get('phone')
        reg.Password = request.POST.get('password')
        reg.save()  
        return redirect('/Registrationdetails', reg_id=reg.id)
    return render(request, 'editregistration.html', {'reg': reg})

def delete_registration(request, id):
    # Retrieve the booking object based on the provided id
    reg = Registration.objects.get(pk=id)
    if request.method == 'POST':
        reg.delete()
        return redirect('/Registrationdetails') 
    return render(request, 'deleteregistration.html', {'reg': reg})         