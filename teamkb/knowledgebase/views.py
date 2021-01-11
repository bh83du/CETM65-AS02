from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Updated view to render home.html
def home(request):
    return render(request, 'knowledgebase/home.html', {'title': 'Homepage'})

class ArticleListView(ListView):
    # Database/Model view will use
    model = Article
    # Add template _name to override defauly of <app>/<model>_<viewtype>.html
    template_name = 'knowledgebase/articles.html'
    # Default is is object_view, add context_object_name to overide this
    context_object_name = 'articles'
    # This will order posts from newest to oldest.
    ordering = ['-date_updated']
    paginate_by = 5

class AuthorArticleListView(ListView):
    model = Article
    template_name = 'knowledgebase/articles_author.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=user).order_by('-date_updated')
    

class ArticleDetailView(DetailView):
    model = Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'jiraid']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/articles/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def news(request):
    return render(request, 'knowledgebase/news.html', {'title': 'News'})
