from django.test import TestCase
from django.urls import resolve
from knowledgebase.views import home, about

class TestHomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

class TestAboutPage(TestCase):
    def test_about_url_resolves_to_about_page_view(self):
        found = resolve('/about/')
        self.assertEqual(found.func, about)    
