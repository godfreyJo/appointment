from django.contrib import admin

from .models import Booking
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    list_display = ['Fname', 'Lname', 'emailAddress', 'phoneNumber', 'booking_date', 'timeStamp']
    form = BookingForm
    list_filter = ['Fname', 'Lname', 'emailAddress', 'phoneNumber', 'booking_date', 'timeStamp']
    search_fields = ['Fname', 'emailAddress', 'phoneNumber', 'booking_date', ]


admin.site.register(Booking, BookingAdmin)
