from django.shortcuts import render
from django.http import HttpResponse

# Dummy post data - Added for initial testing
posts = [
    {
        'author': 'Stuart',
        'title': 'First Post',
        'content': 'This is the content of the first post',
        'date_posted': 'January 3rd, 2021',

    },
    {
        'author': 'Mike',
        'title': 'Second Post',
        'content': 'This is the content of the second post',
        'date_posted': 'January 4th, 2021',

    }
]

# Updated view to render home.html
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'knowledgebase/home.html', context)

# Updated view to render about.html

def about(request):
    return render(request, 'knowledgebase/about.html', {'title': 'About'})
