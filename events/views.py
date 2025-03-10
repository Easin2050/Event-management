from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.forms import EventModelForm,ParticipantForm,CategoryForm
from events.models import Event,Participant,Category

def home_page(request):
     return render(request, "dashboard/homepage.html")

def event_page(request):
     return render(request,"dashboard/event_page.html")

# def create_event(request):
#     participants = Participant.objects.all() 
#     form = EventForm(participants=participants)

#     if request.method == "POST":
#         form = EventForm(request.POST, participants=participants)  
#         if form.is_valid():
#             data = form.cleaned_data
#             name = data.get("name")
#             description = data.get("description")
#             date = data.get("date")
#             time = data.get("time")
#             location = data.get("location")
#             category = data.get("category")  
#             selected_participant = data.get("participants")  
#             event = Event.objects.create(
#                 name=name,
#                 description=description,
#                 date=date,
#                 time=time,
#                 location=location,
#                 category=category,  
#             )
#             for part_id in selected_participant:
#                  participant=Participant.objects.get(id=part_id)
#                  event.participants.add(participant)

#     return render(request, 'event_form.html', {"form": form})
def create_event(request):
    participants = Participant.objects.all()  
    form = EventModelForm()

    if request.method == "POST":
        form = EventModelForm(request.POST)  
        if form.is_valid():
            form.save()
            return render(request, 'event_form.html', {"form": form, "message": "Event added successfully"})
    return render(request, 'event_form.html', {"form": form})

          #   data = form.cleaned_data
          #   name = data.get("name")
          #   description = data.get("description")
          #   date = data.get("date")
          #   time = data.get("time")
          #   location = data.get("location")
          #   category = data.get("category")  
          #   participants = data.get("participants") or [] 

          #   event = Event.objects.create(
          #       name=name,
          #       description=description,
          #       date=date,
          #       time=time,
          #       location=location,
          #       category=category,  
          #   )
          #   event.participants.set(participants)
          # return HttpResponse("Task added successfully")
def create_participant(request):
    form = ParticipantForm()

    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'participant_form.html', {"form": form, "message": "Participant added successfully"})

    return render(request, 'participant_form.html', {"form": form})

def create_category(request):
    form =CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'category_form.html', {"form": form, "message": "Category added successfully"})

    return render(request, 'category_form.html', {"form": form})

def show_dashboard(request):
     return render(request,"dashboard.html")

def base(request):
     return render(request,"dashboard/base.html")

def dashboard(request):
     return render(request,"dashboard/dashboard.html")