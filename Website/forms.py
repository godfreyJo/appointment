from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['Fname', 'Lname', 'emailAddress', 'phoneNumber', 'booking_date', 'timeStamp']