from django.db import models
from datetime import datetime

class Booking(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    emailAddress = models.EmailField(max_length=30)
    phoneNumber = models.CharField(max_length=20)
    booking_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.Fname

