from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q, Count
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from datetime import datetime
from events.forms import EventModelForm, ParticipantForm, CategoryForm
from events.models import Event,Category,RSVP
from django.contrib.auth.models import User


def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_admin_or_organizer(user):
    return is_admin(user) or is_organizer(user)

def home_page(request):
    return render(request, "dashboard/homepage.html")

@login_required
@user_passes_test(is_admin_or_organizer, login_url='no-permission')
@permission_required('events.add_event', login_url='no-permission')
def create_event(request):
    # participants = Participant.objects.all()  
    form = EventModelForm()
    if request.method == "POST":
        form = EventModelForm(request.POST,request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, "Event Created Successfully")
            return redirect('create-event')
    return render(request, 'event_form.html', {"form": form} )

@login_required
@user_passes_test(is_admin, login_url='no-permission')
@permission_required('events.add_participant', login_url='no-permission')
def create_participant(request):
    form = ParticipantForm()
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Participant Created Successfully")
            return redirect('create-participant') 
    return render(request, 'participant_form.html', {"form": form})

@login_required
@user_passes_test(is_admin_or_organizer, login_url='no-permission')
@permission_required('events.add_category', login_url='no-permission')
def create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Created Successfully")
            return redirect('create-category') 
    return render(request, 'category_form.html', {"form": form})

@login_required
@user_passes_test(is_admin_or_organizer, login_url='no-permission')
def dashboard(request):
    today = timezone.now().date()
    event_type = request.GET.get("type", "")
    selected_event_id = request.GET.get("event_id")

    events = Event.objects.select_related('category').prefetch_related('participants').all()

    event_counts = events.aggregate(
        total_events=Count('id'),
        upcoming_events=Count("id", filter=Q(date=today) | Q(date__gt=today)),
        past_events=Count('id', filter=Q(date__lt=today)),
    )
    all_category=Category.objects.all()
    participants = User.objects.filter(is_superuser=False)
    event_participants = Event.objects.aggregate(
        total_participants=Count('participants', distinct=True)
    )
    total_participants = participants.count()

    if event_type == "total_participants":
        events = events.filter(date=today)
    elif event_type == "total_events":
        events = events.all()
    elif event_type == "upcoming_events":
        events = events.filter(date__gte=today)
    elif event_type == "past_events":
        events = events.filter(date__lt=today)
    else:
        events = events.filter(date=today)

    selected_event = None
    participant_users = []

    if selected_event_id:
        selected_event = Event.objects.prefetch_related('participants').filter(id=selected_event_id).first()
        if selected_event:
            participant_users = selected_event.participants.all()

    context = {
        'events': events,
        'participants': participants,
        'total_participants': total_participants,
        'event_counts': event_counts,
        'event_participants': event_participants,
        'participant_users': participant_users,
        'selected_event': selected_event,
        'all_category': all_category,
    }
    return render(request, "dashboard/dashboard.html", context)

def base(request):
    return render(request, "dashboard/base.html")

@login_required
def search(request):
    total_category = Category.objects.all()
    query = request.GET.get('q', '')
    category_query = request.GET.get('type', '')
    events = Event.objects.all()
    first_date = request.GET.get('start_date', '')
    second_date = request.GET.get('end_date', '')

    if first_date and second_date:
        events = events.filter(date__gte=first_date, date__lte=second_date)

    if category_query:
        events = events.filter(category__name=category_query)

    if query:
        events = events.filter(
            Q(name__icontains=query) | 
            Q(location__icontains=query)
        ).distinct()

    for event in events:
        event.participant_count = event.participants.count() 
    
    context = {
        'events': events,
        'query': query,
        'total_category': total_category,
        'is_admin': is_admin(request.user),
        'is_organizer': is_organizer(request.user),
    } 
    return render(request, 'dashboard/search_page.html', context)

@login_required
@permission_required('events.change_event', login_url='no-permission')
def update_event(request, id):
    events = Event.objects.get(id=id)
    form = EventModelForm(instance=events)
    if request.method == "POST":
        form = EventModelForm(request.POST, instance=events)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated Successfully")
            return redirect('update', id)
    return render(request, 'event_form.html', {"form": form}) 

@login_required
@permission_required('events.delete_event', login_url='no-permission')
def delete_event(request, id):
    if request.method == "POST":
        events = Event.objects.get(id=id)
        events.delete()
        messages.success(request, "Event deleted Successfully")
        return redirect('dashboard')
    else:
        messages.error(request, "Something went wrong")
        return redirect('dashboard')

@login_required
def event_page(request, id):
    event = Event.objects.get(id=id)
    event_participants = event.participants.all()
    context = {
        'event': event,
        'event_participants': event_participants
    }
    return render(request, 'dashboard/event_page.html', context)

@login_required
@permission_required('events.change_participant', login_url='no-permission')
def update_participant(request, id):
    participant = User.objects.get(id=id)
    form = ParticipantForm(instance=participant)
    if request.method == "POST":
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, "Participant updated Successfully")
            return redirect('participant_page')
    return render(request, 'participant_form.html', {"form": form}) 

@login_required
@permission_required('events.delete_participant', login_url='no-permission')
def delete_participant(request, id):
    if request.method == "POST":
        participant = User.objects.get(id=id)
        participant.delete()
        messages.success(request, "Participant deleted Successfully")
        return redirect('participant_page')
    else:
        messages.error(request, "Something went wrong")
        return redirect('dashboard')

@login_required
@permission_required('events.change_category', login_url='no-permission')
def update_category(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated Successfully")
            return redirect('dashboard')
    return render(request, 'category_form.html', {"form": form}) 

@login_required
@permission_required('events.delete_category', login_url='no-permission')
def delete_category(request, id):
    if request.method == "POST":
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, "Category deleted Successfully")
        return redirect('dashboard')
    else:
        messages.error(request, "Something went wrong")
        return redirect('dashboard')

@login_required
def user_dashboard(request):
    rsvp_events = RSVP.objects.filter(user=request.user)
    return render(request, 'dashboard/user_dashboard.html', {'rsvps': rsvp_events})


@login_required
def rsvp_event(request, event_id):
    event = Event.objects.get(id=event_id)

    if RSVP.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, "You have already RSVP to this event.")
    else:
        RSVP.objects.create(user=request.user, event=event)
        event.participants.add(request.user)
        messages.success(request, "Successfully RSVP for the event!")

    return redirect('user_dashboard')


@login_required
def rsvp_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    rsvp = RSVP.objects.filter(user=request.user, event=event).first()
    if rsvp:
        rsvp.delete()
        event.participants.remove(request.user)
        messages.success(request, "Successfully removed RSVP for the event!")
    else:
        messages.warning(request, "You have not RSVP'd to this event.")

    return redirect('user_dashboard')


@login_required
@user_passes_test(is_admin, login_url='no-permission')
def participant_page(request):
    participants = User.objects.filter()
    context = {
        'participants': participants,
    }
    return render(request,'dashboard/participant_page.html',context)