from django.test import RequestFactory,TestCase
from django.urls import resolve
from knowledgebase.views import home
from .models import Article, Category, Area
from users.models import User
from .views import ArticleListView, AuthorArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, SearchResultsView
from .forms import CreateArticleForm, UpdateArticleForm


# Test Knowledgebase Models
class KnowledgebaseModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='mzy8mh',
            first_name='Test',
            last_name='User',
            email='test.user@testcompany.co.uk',
            password='Testing321',
        )

    # Test Article Model is as expected.   
    def test_article_model(self):
        article = Article()
        article.title='Test'
        article.author=User.objects.get(pk=1)
        article.content='TestContent'
        article.jiraid='ELCSS-2021'
        article.category='Testing'
        article.area='DevPortal'

        article.save()
       
        saved_articles = Article.objects.all()
        self.assertEqual(saved_articles.count(), 1)

        saved_art = saved_articles[0]
        self.assertEqual(saved_art.title, 'Test')
        self.assertEqual(saved_art.author, User.objects.get(pk=1))
        self.assertEqual(saved_art.content, 'TestContent')
        self.assertEqual(saved_art.jiraid, 'ELCSS-2021')
        self.assertEqual(saved_art.category, 'Testing')
        self.assertEqual(saved_art.area, 'DevPortal')



    # Test Category Model is as expected.
    def test_category_model(self):
        category = Category()
        category.name='Testing'

        category.save()

        saved_cats = Category.objects.all()
        self.assertEqual(saved_cats.count(), 1)

        saved_cat = saved_cats[0]
        self.assertEqual(saved_cat.name, 'Testing')

    def test_area_model(self):
        area = Area()
        area.func_area = 'DevPortal'

        area.save()

        saved_areas = Area.objects.all()
        self.assertEqual(saved_areas.count(), 1)

        saved_area = saved_areas[0]
        self.assertEqual(saved_area.func_area, 'DevPortal')


# Test Knowledgebase Views

class TestHomePage(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

class ArticleListViewTest(TestCase):
    def test_ArticleListView(self):
        response = self.client.get('/articles/')
        self.assertTemplateUsed(response, 'knowledgebase/articles.html')

class AuthorArticleListViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(
        username='mzy8mh',
        first_name='Test',
        last_name='User',
        email='test.user@testcompany.co.uk',
        password='Testing321',
    )

    def test_AuthorArticleListView(self):
        response = self.client.get('/user/mzy8mh/')
        self.assertTemplateUsed(response, 'knowledgebase/articles_author.html')        

class ArticleDetailViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(
        username='mzy8mh',
        first_name='Test',
        last_name='User',
        email='test.user@testcompany.co.uk',
        password='Testing321',
    )
        article = Article.objects.create(
        title='Test',
        author=User.objects.get(pk=1),
        content='TestContent',
        jiraid='ELCSS-2021',
        category='Testing',
        area='DevPortal',
        )

    def test_ArticleListView(self):
        response = self.client.get('/knowledgebase/1/')
        self.assertTemplateUsed(response, 'knowledgebase/article_detail.html')

class ArticleCreateViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(
        username='mzy8mh',
        first_name='Test',
        last_name='User',
        email='test.user@testcompany.co.uk',
        password='Testing321',
        )
        
    def test_ArticleCreateView(self):
        response = self.client.get('/knowledgebase/create')
        self.assertIsInstance(response.context['form'], CreateArticleForm)


class ArticleUpdateViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(
        username='mzy8mh',
        first_name='Test',
        last_name='User',
        email='test.user@testcompany.co.uk',
        password='Testing321',
    )
        article = Article.objects.create(
        title='Test',
        author=User.objects.get(pk=1),
        content='TestContent',
        jiraid='ELCSS-2021',
        category='Testing',
        area='DevPortal',
        )


    def test_ArticleUpdateView(self):
        response = self.client.get('/knowledgebase/1/update')
        self.assertIsInstance(response.context['form'], UpdateArticleForm)
    
class ArticleDeleteViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(
        username='mzy8mh',
        first_name='Test',
        last_name='User',
        email='test.user@testcompany.co.uk',
        password='Testing321',
    )
        article = Article.objects.create(
        title='Test',
        author=User.objects.get(pk=1),
        content='TestContent',
        jiraid='ELCSS-2021',
        category='Testing',
        area='DevPortal',
        )

    def test_ArticleDeleteView(self):
        response = self.client.get('/knowledgebase/1/delete/')
        self.assertTemplateUsed(response, 'knowledgebase/article_confirm_delete.html')