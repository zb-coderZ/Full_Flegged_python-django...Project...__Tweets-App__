from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'website/home.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')

def privacy_view(request):
    return render(request,'website/privacy.html')