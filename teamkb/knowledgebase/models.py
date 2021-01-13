from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Creating a model to store knowledge base articles
class Article(models.Model):
    title = models.CharField(max_length=80, unique=True, null=False)
    category = models.CharField(max_length=30, null=False)
    area = models.CharField(max_length=30, blank=True, null=False)
    content = RichTextField()
    jiraid = models.CharField(max_length=80, blank=True, null=True, verbose_name='Jira ID')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT) # Doesn't delete post when Author is deleted.
    
# Add __str__ method to be returned when model is queried.

    def __str__(self):
        article_str =   f"ID: {self.id}" \
                        f"Title: {self.title}" \
                        f"Area: {self.area}" \
                        f"Content: {self.content}" \
                        f"Jira ID: {self.jiraid}" \
                        f"Date Posted: {self.date_posted}" \
                        f"Date Updated: {self.date_updated}" \
                        f"Author: {self.author}" \
        
        return article_str 

    def get_absolute_url(self):
        return reverse('KB-detail', kwargs={'pk': self.pk})


# Create a model to maintain Article Categories

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True, null=False)

    def __str__(self):
        category_str =   f"Name: {self.name}"
        return category_str 

    def get_absolute_url(self):
        return reverse('KB-detail', kwargs={'pk': self.pk})


# Create a model to maintain Functional Areas

class Area(models.Model):
    func_area = models.CharField(max_length=80, unique=True, null=False)

    def __str__(self):
        category_str =   f"Functional Area: {self.func_area}"
        return category_str 

    def get_absolute_url(self):
        return reverse('KB-detail', kwargs={'pk': self.pk})    


