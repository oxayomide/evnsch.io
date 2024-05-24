# events/forms.py
from django import forms
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'start_time', 'end_date', 'end_time']



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
