from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration

# Sign Up view.  User Creation Form
def signup(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Success!  Sign up completed for {username}.') 
            return redirect('KB-home')
    else:
        form = UserRegistration()
    return render(request, 'users/signup.html', {'form': form})