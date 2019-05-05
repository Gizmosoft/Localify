from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    # return HttpResponse('Hello World!')
    template_name = 'test.html'
