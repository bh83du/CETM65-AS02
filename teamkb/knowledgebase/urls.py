from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, AuthorArticleListView

# Included URL patterns
urlpatterns = [
    path('', views.home, name='KB-home'),
    path('user/<str:username>/', AuthorArticleListView.as_view(), name='KB-author'),
    path('articles/', ArticleListView.as_view(), name='KB-articles'),
    path('knowledgebase/<int:pk>/', ArticleDetailView.as_view(), name='KB-detail'),
    path('knowledgebase/create/', ArticleCreateView.as_view(), name='KB-create'),
    path('knowledgebase/<int:pk>/update', ArticleUpdateView.as_view(), name='KB-update'),
    path('knowledgebase/<int:pk>/delete', ArticleDeleteView.as_view(), name='KB-delete'),
    path('news/', views.news, name='KB-news'),
]


