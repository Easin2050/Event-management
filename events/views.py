from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
     return render(request, "dashboard/homepage.html")

def event_page(request):
     return render(request,"dashboard/event_page.html")