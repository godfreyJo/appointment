from django.db import models
from datetime import datetime

class Booking(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    emailAddress = models.EmailField(max_length=30)
    phoneNumber = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    your_message = models.TextField(max_length=200)
    def __str__(self):
        return self.Fname

