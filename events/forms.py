from django import forms
from django.forms import SelectDateWidget, TimeInput
from events.models import Category,Participant,Event

# Django Model form
class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category', 'participants']
        widgets={
            'date':forms.SelectDateWidget,
            'time':forms.TimeInput
        }
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
