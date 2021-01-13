from django import forms
from .models import Article, Category, Area

cats = Category.objects.all().values_list('name','name')

cats_list = []

for item in cats:
    cats_list.append(item)

area = Area.objects.all().values_list('func_area','func_area')

area_list = []

for item in area:
    area_list.append(item)

class CreateArticleForm(forms.ModelForm):
    class Meta:
            model = Article
            fields = ['title', 'category', 'area', 'content', 'jiraid']

            widgets = {
                'title':    forms.TextInput(attrs={'placeholder': 'Enter Article Title...'}),
                'area':     forms.Select(choices=area_list),
                'category': forms.Select(choices=cats_list),
                'jiraid':   forms.TextInput(attrs={'placeholder': 'Enter Relevant JIRA IDs...'})
            }

class UpdateArticleForm(forms.ModelForm):
    class Meta:
            model = Article
            fields = ['title', 'category', 'area', 'content', 'jiraid']

            widgets = {
                'category': forms.Select(choices=cats_list)
            }

