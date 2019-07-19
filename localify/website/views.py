from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
# from .geolocation import Geolocation

# Create your views here.
# class HomePageView(TemplateView):
#     # return HttpResponse('Hello World!')
#     template_name = 'home.html'

def home_page(request):
    context = {"home_page": "active"}
    return render(request,"home.html",context)

def user_profile(request):
    # superusers_username = User.objects.filter(is_superuser=True).values_list('username', flat=True).get(pk=1)
    # context={
    #     "usr" : superusers_username
    # }
    return render(request,"profile.html")

def login_page(request):
    return render(request,"login.html")


# Retreiving location using IPstack
# def home_page(request):
#     location_info = Geolocation()
#     context={
#         "loc" : location_info
#     }
#     if request.method == "POST":
#         print(request.POST.get('user_city'))
#         print(request.POST.get('user_zip'))
#     return render(request,"home.html",context)
