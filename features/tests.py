from django.test import TestCase
from django.test import Client
from django.urls import reverse
from features.models import *

# Create your tests here.
class URLTests(TestCase):
    def test_dashboard(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_on_demand(self):
        response = self.client.get(reverse('available'))
        self.assertEqual(response.status_code, 302)

    def test_view_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_spointment(self):
        response = self.client.get(reverse('appointment'))
        self.assertEqual(response.status_code, 200)


class ModelTests(TestCase):
    def test_user(self):
        Person.objects.create(username="John", email="john@gmail.com", professional=True, on_demand=True)
        user = Person.objects.get(username="John")

        self.assertEqual(user.username, "John")
        self.assertEqual(user.email, "john@gmail.com")
        self.assertTrue(user.professional)
        self.assertTrue(user.on_demand)

    def test_appointment(self):
        Appointment.objects.create(health_professional_username="John",
                                              user_username="Chris",
                                              first_name= "Chris",
                                              last_name="Smith",
                                              email="chris@gmail.com",
                                              phone="123456"
                                   )
        appointment = Appointment.objects.get(health_professional_username="John")

        self.assertEqual(appointment.health_professional_username, "John")
        self.assertEqual(appointment.user_username, "Chris")
        self.assertEqual(appointment.first_name, "Chris")
        self.assertEqual(appointment.last_name, "Smith")
        self.assertEqual(appointment.email, "chris@gmail.com")
        self.assertEqual(appointment.phone, "123456")

    def test_chat_room(self):
        ChatRoom.objects.create(url="google.com")
        room = ChatRoom.objects.get(url="google.com")

        self.assertEqual(room.url, "google.com")

class ViewsTests(TestCase):
    def test_dashboard_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed('index.html')

    def test_register_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed('register.html')

    def test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed('login.html')

    def test_on_demand_template(self):
        response = self.client.get(reverse('available'))
        self.assertTemplateUsed('on-demand.html')

    def test_view_profile_template(self):
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed('profile.html')

    def test_appointment_template(self):
        response = self.client.get(reverse('appointment'))
        self.assertTemplateUsed('appointment.html')

