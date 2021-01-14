from django.test import TestCase
from django.urls import resolve
from knowledgebase.views import home
from .models import Article, Category, Area
from users.models import User


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



class TestHomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
