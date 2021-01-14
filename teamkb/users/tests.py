from django.test import TestCase
from knowledgebase.models import Article, Category, Area
from .models import User, Profile
# Create your tests here.

# Test Users Model
class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(
            username='mzy8mh',
            first_name='Test',
            last_name='User',
            email='test.user@testcompnay.co.uk',
            password='Testing321',
        )

    def test_user_table(self):
        user = User()
        user.username='john'
        user.first_name='John'
        user.last_name='Smith'
        user.email='john.smith.test.co.uk'
        user.password='Testing123'

        user.save()
        expected = User.objects.get(pk=2)
        self.assertEqual(expected, user)

    def test_profile_table(self):
        profile = Profile.objects.get(pk=1)
        profile.image='default.jpg'
        profile.bio='Test Biography'

        profile.save()
        expected = Profile.objects.get(pk=1)
        self.assertEqual(expected, profile)


