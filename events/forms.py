from django import forms

class EventForm(forms.Form):
    name=forms.CharField(max_length=250,label="Event Name")
    description=forms.CharField(widget=forms.Textarea,label="Event Description")
    date=forms.DateField(widget=forms.SelectDateWidget)
    time=forms.TimeField()
    location=forms.CharField()
    Catagory=forms.CheckboxSelectMultiple()


class ParticipantForm(forms.Form):
    name=forms.CharField(max_length=250,label="Participant Name")
    email=forms.EmailField(label="Email")

class Catagory(forms.Form):
    name=forms.CharField(label="Catagoty Name")
    description=forms.CharField(widget=forms.Textarea,label="Description")