from django import forms
from django.forms import SelectDateWidget, TimeInput
from events.models import Category,Participant,Event

# class EventForm(forms.Form):
#     name = forms.CharField(max_length=255, label="Event Name")
#     description = forms.CharField(widget=forms.Textarea, label="Event Description")
#     date = forms.DateField(label="Event Date", widget=forms.SelectDateWidget())
#     time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}), label="Event Time")
#     location = forms.CharField(max_length=255, label="Event Location")
#     # event_participant = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)    
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category", label="Category")    
#     # def __init__(self, *args, **kwargs):
#     #     participants = kwargs.pop("participants", [])  
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['event_participant'].choices = [(pat.id, pat.name) for pat in participants]

#     participants = forms.ModelMultipleChoiceField(
#         queryset=Participant.objects.all(),
#         widget=forms.CheckboxSelectMultiple,  
#         label="Select Participants"
#     )

#     def __init__(self, *args, **kwargs):
#         participants = kwargs.pop("participants", [])  
#         super().__init__(*args, **kwargs)
#         self.fields['participants'].queryset = participants


# class StyleFormMixin:
#     default_classes = "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2"

#     def apply_styled_widget(self):
#         """
#         Apply consistent styling to form fields based on their widget types.
#         """
#         for field_name, field in self.fields.items():
#             # Apply default classes to all widgets
#             field.widget.attrs.update({
#                 'class': self.default_classes
#             })

#             # Add placeholder for text inputs and textareas
#             if isinstance(field.widget, forms.TextInput):
#                 field.widget.attrs.update({
#                     'placeholder': f"Enter {field.label.lower()}"
#                 })
#             elif isinstance(field.widget, forms.Textarea):
#                 field.widget.attrs.update({
#                     'placeholder': f"Enter {field.label.lower()}"
#                 })

#             # Custom styling for SelectDateWidget
#             if isinstance(field.widget, forms.SelectDateWidget):
#                 field.widget.attrs.update({
#                     'class': "border-2 border-gray-300 rounded-lg shadow-sm p-2 bg-green-500"
#                 })

#             # Custom styling for CheckboxSelectMultiple
#             if isinstance(field.widget, forms.CheckboxSelectMultiple):
#                 field.widget.attrs.update({
#                     'class': "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2"
#                 })
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
    
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.apply_styled_widget()

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

   

        # You can add additional customization here if needed
    # name = forms.CharField(max_length=255, label="Participant Name")
    # email = forms.EmailField(label="Email")



from django import forms
from .models import Category

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # name = forms.CharField(label="Category Name")
    # description = forms.CharField(widget=forms.Textarea, label="Description")
    