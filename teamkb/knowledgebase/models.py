from django.db import models
from django.contrib.auth.models import User


# Creating a model to store knowledge base articles
class Article(models.Model):
    title = models.CharField(max_length=80, unique=True, null=False)
    area = models.CharField(max_length=30, null=False)
    content = models.TextField()
    jiraid = models.CharField(max_length=80, null=True)
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



