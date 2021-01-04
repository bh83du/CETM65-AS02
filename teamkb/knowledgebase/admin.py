from django.contrib import admin
# Import the model (table) Article
from .models import Article

#Register the model to be viewable through the Admin Site.
admin.site.register(Article)


