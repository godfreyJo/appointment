"""DenWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Website import views
# from . import views

urlpatterns = [
	path('', include('Website.urls')),
    path('pricing.html', views.pricing, name="pricing"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('blog.html', views.blog, name="blog"),
    path('blog-details.html', views.blogDetails, name="blogDetails"),
    path('admin/', admin.site.urls),
]
