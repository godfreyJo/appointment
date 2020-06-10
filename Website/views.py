from django.shortcuts import render, redirect
from django.core.mail import send_mail
from Website.forms import BookingForm
from .models import Booking


def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def booking(request):
	form = BookingForm()
	if request.method == 'POST':
		# print('Printing Post', request.POST)
		form = BookingForm(request.POST or None)
		if form.is_valid():
			form.save()		
			return redirect('/')
	
	args = {'form':form}
	return render(request, 'booking.html', args)

def blog(request):
	return render(request, 'blog.html', {})

def blogDetails(request):
	return render(request, 'blog-details.html', {})

def contact(request):
	if request.method == "POST":
		# do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# Send email
		send_mail(
			message_name,# subject
			message, # message
			message_email, # from email
			['godfreyoyugi@gmil.com'],# to Email
			fail_silently=False,
			)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
		# return the page
		return render(request, 'contact.html', {})


