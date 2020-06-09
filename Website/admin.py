from django.contrib import admin

from .models import Booking
from .forms import BookingForm

class BookingAdmin(admin.ModelAdmin):
    list_display = ['Fname', 'Lname', 'emailAddress', 'phoneNumber', 'date', 'timeStamp','your_message']
    form = BookingForm
    list_filter = ['Fname', 'Lname', 'emailAddress', 'phoneNumber', 'date', 'timeStamp','your_message']
    search_fields = ['Fname', 'emailAddress', 'phoneNumber', 'date', ]


admin.site.register(Booking, BookingAdmin)
