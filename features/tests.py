from django.test import TestCase
from features.models import *

# Create your tests here.

class URLTests(TestCase):
    def test_dashboard(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        
# class ModelTests(TestCase):
#     def test_user(self):
#         User.objects.create(user_name= "John", user_contact = "000", user_photo="photo", user_email="john@gmail.com", user_active_status=True)
#         user = User.objects.get(user_name="John")
# 
#         self.assertEqual(user.user_name, "John")
#         self.assertEqual(user.user_contact, "000")
#         self.assertEqual(user.user_photo, "photo")
#         self.assertEqual(user.user_email, "john@gmail.com")
#         self.assertTrue(user.user_active_status)

# class ViewsTests(TestCase):
#     def test_homepage(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed('home.html')