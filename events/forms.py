from django import forms
from events.models import Category,Event
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User
from django.db.models import Q



class StyledFormMixin:
    """Mixin to apply consistent styling to form fields"""
    default_classes = "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2 focus:outline-none focus:border-rose-500 focus:ring-rose-500"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows': 4
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": f"{self.default_classes} bg-green-500"
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    "class": self.default_classes,
                    "type": "time"
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    "class": self.default_classes
                })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    "class": self.default_classes,
                    "type": "email",
                    "placeholder": f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    "class": "space-y-2"
                })
            else:
                field.widget.attrs.update({
                    "class": self.default_classes
                })


class EventModelForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category', 'participants','asset']
        widgets = {
            'date': forms.SelectDateWidget(),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'participants': forms.CheckboxSelectMultiple()
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


class ParticipantForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(Q(email=email) | Q(username=username)).exists():
            raise ValidationError("A user with this email or username already exists.")
        return email

class CategoryForm(StyledFormMixin, forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']
