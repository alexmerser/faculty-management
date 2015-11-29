from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client


class TestHome(TestCase):
    def test_single(self):
        self.client = Client()
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        response = self.client.get('/')
        self.assertContains(response, 'Assignments')
        self.assertContains(response, 'Researches')
        self.assertEqual(response.status_code, 200)
