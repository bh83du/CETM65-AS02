from django.test import TestCase
from knowledgebase.models import Article, Category, Area
from .models import User, Profile
from django.contrib.auth import views as auth_views
from .forms import UserRegistration, UserUpdateForm, ProfileUpdateForm

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
        user.email='john.smith@test.co.uk'
        user.password='Testing123'

        user.save()

        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 2)
        # Confirm number of records saved to DB
        saved_user = saved_users[1]
        self.assertEqual(saved_user.username, 'john')
        self.assertEqual(saved_user.first_name, 'John')
        self.assertEqual(saved_user.last_name, 'Smith')
        self.assertEqual(saved_user.email, 'john.smith@test.co.uk')
        self.assertEqual(saved_user.password, 'Testing123')
        # Confirm content of record saved to DB
        
    def test_profile_table(self):
        profile = Profile.objects.get(pk=1)
        profile.image='default.jpg'
        profile.bio='Test Biography'

        profile.save()

        saved_profs = Profile.objects.all()
        self.assertEqual(saved_profs.count(), 1)

        saved_prof = saved_profs[0]
        self.assertEqual(saved_prof.image, 'default.jpg')
        self.assertEqual(saved_prof.bio, 'Test Biography')

class UsersViews(TestCase):
    # Unit tests for Views and Forms in the Users App
    # Confirming the correct template is returned
    # Confirming the correct form is returned (where applicable)
    def setUp(self):
        User.objects.create(
        username='mzy8mh',
        first_name='Test',
        last_name='User',
        email='test.user@testcompnay.co.uk',
        password='Testing321',
    )

    def test_loginview(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'users/login.html')
        
    
    def test_password_reset(self):
        response = self.client.get('/reset_password/')
        self.assertTemplateUsed(response, 'users/reset_password.html')

    def test_password_reset_sent(self):
        response = self.client.get('/reset_password_sent/')
        self.assertTemplateUsed(response, 'users/password_reset_sent.html')

    def test_password_reset_complete(self):
        response = self.client.get('/reset_password_complete/')
        self.assertTemplateUsed(response, 'users/password_reset_done.html')

    def test_logout_view(self):
        response = self.client.get('/logout/')
        self.assertTemplateUsed(response, 'users/logout.html')

    def test_signup_view(self):
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, 'users/signup.html')
        self.assertIsInstance(response.context['form'], UserRegistration)   

    def test_profile_view(self):
        response = self.client.get('/profile/')
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertIsInstance(response.context['form'], ProfileUpdateForm)   


    
