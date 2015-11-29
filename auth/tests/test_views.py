from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.test import TestCase,Client

from courses.models import Course
from subjects.models import Subject
from users.models import Student, Staff


class TestLogin(TestCase):
    def test_user_login(self):
        self.client = Client()
        self.username = 'vba'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        response = self.client.get('/exams/')
        self.assertContains(response,"logout")
        self.assertEqual(response.status_code, 200)