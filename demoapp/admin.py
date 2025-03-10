from django.contrib import admin
from .models import TourBooking
from .models import ContactMessage

@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'tour_package', 'start_date', 'end_date', 'num_travelers')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)