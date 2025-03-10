from django.db import models
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    description=models.TextField()
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title

class TourBooking(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    
    # Tour Package Information
    TOUR_PACKAGE_CHOICES = [
        ('western-ghats-tour', 'Western Ghats Waterfall Tour'),
        ('north-east-expedition', 'North-East India Waterfall Expedition'),
        ('kerala-wellness-retreat', 'Kerala Waterfall & Wellness Retreat'),
    ]
    tour_package = models.CharField(
        max_length=50,
        choices=TOUR_PACKAGE_CHOICES,
        verbose_name="Tour Package"
    )
    
    # Travel Dates
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    
    # Travelers
    num_travelers = models.PositiveIntegerField(verbose_name="Number of Travelers")

    def __str__(self):
        return f"{self.full_name} - {self.tour_package}"


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.email}"

