from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create a new form that inherits from the UserCreationForm

class UserRegistration(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    # Meta class to identify the model for the form to interact with
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # Meta class to identify the model for the form to interact with
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    # Meta class to identify the model for the form to interact with
    class Meta:
        model = Profile
        fields = ['image', 'bio']