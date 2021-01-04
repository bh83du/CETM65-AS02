from django.urls import path
from . import views

# Included URL patterns
urlpatterns = [
    path('', views.home, name='KB-home'),
    path('about/', views.about, name='KB-about'),
]


