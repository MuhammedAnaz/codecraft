from django.shortcuts import render,redirect
from app1.models import Registration, Booking,Contact
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import authenticate, login





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

def login(request):
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

# def adminlogin_view(request):
#     # Check if it's a POST request
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication was successful
#         if user is not None:
#             # Login the user
#             login(request, user)
#             return HttpResponse('Login Successful')
#         else:
#             return HttpResponse('Invalid Login Credentials')
#     else:
#         # Render the login form
#         return render(request, 'login.html')   


def adminlogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('index.html')  # Redirect to the admin dashboard page
        else:
            error_message = 'Invalid credentials'
    else:
        error_message = None

    return render(request, 'adminlogin.html', {'error_message': error_message})


    
        




