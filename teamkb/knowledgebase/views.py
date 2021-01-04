from django.shortcuts import render
from django.http import HttpResponse

# Initial landing response for Home page.
def home(request):
    return HttpResponse('<h1>Knowledge Base Home</h1>')

# Add an 'About' Page

def about(request):
    return HttpResponse('<h1>Knowledge Base About</h1>')
