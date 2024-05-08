from django import forms
from .models import Candidate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'description']

class VoterRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
