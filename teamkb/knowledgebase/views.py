from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Updated view to render home.html
def home(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'knowledgebase/home.html', context)

# Updated view to render about.html

def about(request):
    return render(request, 'knowledgebase/about.html', {'title': 'About'})
