from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import Driver, Booking


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Route after logging in
            return redirect('makeBooking')
        else:
            return render(request,'app/login.html',{messages.info('Invalid Credentials')})
        
    return render(request, 'app/login.html')

def driverLogin(request, id):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(id=id)
            driver = authenticate(request, username=username, password=password)
            if Driver.objects.filter(email = user.email):
                login(request, driver)
                return redirect('bookings')
            else:
                return render(request,'app/driverLogin.html')
            
        return render(request, 'app/driverLogin.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpass = request.POST.get('confpass')

        if password == confpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken. Try another one.")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name = firstname,
                    username = username,
                    email = email,
                    password = password,
                )
                user.set_password(password)
                user.save()
                return redirect('home')
        else:
            messages.info(request, "Passwords doesn't match..")
            return redirect('register')
    else:
        return render(request, 'app/register.html')

def driverRegister(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpass = request.POST.get('confpass')

        if password == confpass:
            if Driver.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken. Try another one.")
                return redirect('driverRegister')
            else:
                driver = Driver.objects.create(
                    firstname = firstname,
                    username = username,
                    email = email,
                    password = password,
                )
                driver.save()
                return redirect('driverLogin')
        else:
            messages.info(request, "Passwords doesn't match.." )
            return redirect('driverRegister')
    else:
        return render(request, 'app/driverRegister.html')

def bookings(request):
    books = list(Booking.objects.all())
    return render(request, 'app/bookings.html',{'books':books})

def mybookings(request):
    datas = list(Booking.objects.all())
    return render(request, 'app/mybookings.html', {'datas':datas})

def makeBooking(request):
   if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('to')
        location = request.POST.get('location')
        pickup = request.POST.get('time')
        phone = request.POST.get('phone')

        booking = Booking.objects.create(
            origin = origin,
            destination = destination,
            location = location,
            pickup = pickup,
            phone = phone,
        )
        booking.save()
        return redirect('mybookings')
   else:
    return render(request, 'app/makeBooking.html')
   

def viewBooking(request, id):
    single_booking = get_object_or_404(Booking, pk=id)
    return render(request, 'app/viewbooking.html', {'single_booking':single_booking})

def driverbookingView(request, id):
    driver_booking = get_object_or_404(Booking, pk=id)
    return render(request, 'app/driverbookingview.html', {'driver_booking':driver_booking})

def billpage(request, id):
    bill_data = get_object_or_404(Booking,pk=id)
    return render(request, 'app/billpage.html', {'bill_data':bill_data})

def logoutApp(request):
    logout(request)
    return redirect(home)


