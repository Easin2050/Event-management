from django import forms
from django.forms import SelectDateWidget, TimeInput

class EventForm(forms.Form):
    name = forms.CharField(max_length=250, label="Event Name")
    description = forms.CharField(widget=forms.Textarea, label="Event Description")
    date = forms.DateField(widget=SelectDateWidget(label="Event Date"))
    time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}), label="Event Time")
    location = forms.CharField(max_length=250, label="Event Location")

class ParticipantForm(forms.Form):
    name = forms.CharField(max_length=250, label="Participant Name")
    email = forms.EmailField(label="Email")

class CategoryForm(forms.Form):
    name = forms.CharField(label="Category Name")
    description = forms.CharField(widget=forms.Textarea, label="Description")