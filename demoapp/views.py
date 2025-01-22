from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TourBooking

# Create your views here.

def home(request):
    if request.method=='POST':
        # Personal Information
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']

        # Tour Package Information
        tour_package = request.POST['tour-package']

        # Travel Dates and Travelers
        start_date = request.POST['start-date']
        end_date = request.POST['end-date']
        num_travelers = request.POST['num-travelers']

        # Save to database
        tour_booking = TourBooking(
            full_name=full_name,
            email=email,
            phone=phone,
            tour_package=tour_package,
            start_date=start_date,
            end_date=end_date,
            num_travelers=num_travelers,
        )
        tour_booking.save()
        return redirect('ThankYou.html')
    return render(request, 'base.html')
def thank_you(request):
    return render(request, 'ThankYou.html')