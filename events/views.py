from django.shortcuts import render
from django.http import HttpResponse
from events.forms import EventForm

def home_page(request):
     return render(request, "dashboard/homepage.html")

def event_page(request):
     return render(request,"dashboard/event_page.html")

def create_event(request):
     form=EventForm()
     return render(request,'event_form.html',{"form":form})

def show_dashboard(request):
     return render(request,"dashboard.html")

def base(request):
     return render(request,"dashboard/base.html")