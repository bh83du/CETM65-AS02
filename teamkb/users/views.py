from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration

# Sign Up view.  User Creation Form
def signup(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Success!  Account created for {username}.  Please login.') 
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'users/signup.html',  {'title': 'Sign Up', 'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})