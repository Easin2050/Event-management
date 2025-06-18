from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def no_permission(request):
    return render(request,'no_permission.html')

# This part is write using chat gpt for render.Please don't consider it as a copy paste code.
def ping(request):
    return HttpResponse("pong")