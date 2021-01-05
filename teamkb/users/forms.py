from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create a new form that inherits from the UserCreationForm

class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    # Meta class to identify the model for the form to interact with
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']