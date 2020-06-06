from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('pricing.html', views.pricing, name="pricing"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('blog.html', views.blog, name="blog"),
    path('booking.html', views.booking, name="booking"),
    
]
