# from django.contrib import admin
# from .models import Blog,TourBooking
# # Register your models here.
# admin.site.register(Blog)
# admin.site.register(TourBooking)

from django.contrib import admin
from .models import TourBooking

@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'tour_package', 'start_date', 'end_date', 'num_travelers')
