from django.contrib import admin
from .models import Article, Category, Area

# Register models to be viewable through the Admin Site.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Area)



