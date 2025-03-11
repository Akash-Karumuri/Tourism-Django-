from django.shortcuts import render,redirect
from .models import TourBooking
from django.contrib import messages
from .models import ContactMessage


def home(request):
    if request.method=='POST':
        # Personal Information
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        tour_package = request.POST.get('tour-package', '').strip()
        start_date = request.POST.get('start-date', '').strip()
        end_date = request.POST.get('end-date', '').strip()
        num_travelers = request.POST.get('num-travelers', '').strip()
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
        messages.success(request, "Your booking has been submitted successfully!")
        return redirect('/#packages')

    return render(request, 'base.html')



def contact_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        # Save the message to the database
        ContactMessage.objects.create(full_name=full_name, email=email, message=message)
        
        # Show success message
        messages.success(request, "Your message has been sent successfully!")

        # Redirect back to the homepage at the contact section
        return redirect("/#sign")  

    return render(request, "base.html")


