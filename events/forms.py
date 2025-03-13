from django import forms
from events.models import Category,Participant,Event
from django.core.exceptions import ValidationError
from datetime import date

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category', 'participants']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'placeholder': "Enter Event Name"
            }),
            'description': forms.Textarea(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'placeholder': "Write a short event description",
            }),
            'date': forms.SelectDateWidget(attrs={
                'class': "border-2 border-gray-300 rounded-lg shadow-sm p-2 bg-green-500"
            }),
            'time': forms.TimeInput(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'type': 'time'
            }),
            'location': forms.TextInput(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'placeholder': "Enter Event Location"
            }),
            'category': forms.Select(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2"
            }),
            'participants': forms.CheckboxSelectMultiple(attrs={  
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2"
            })
        }

    def clean_date(self):
        event_date = self.cleaned_data.get('date')
        if event_date is None:
            raise ValidationError("Event date is required.") 
        if not isinstance(event_date, date):
            raise ValidationError("Invalid date format.")
        if event_date < date.today():
            raise ValidationError("You cannot create an event with a past date.")
        return event_date 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select Category"
    
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'placeholder': "Enter Participant Name"  
            }),
            'email': forms.EmailInput(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'placeholder': "Enter Email Here",
                'type': 'email' 
            })
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'placeholder': "Enter Category Name"  
            }),
            'description': forms.Textarea(attrs={
                'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2",
                'placeholder': "Write a short category description",
                'rows': 4 
            })
        }
