from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from courses.models import Course
from subjects.models import Subject
from users.models import Staff


class TestSubjectList(TestCase):
    def test_single_list(self):
        self.client = Client()
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        course = Course.objects.create(number='1234', name='Test course')
        staff = Staff.objects.create(
            user=User.objects.create_user('test_staff', first_name='Staff')
        )
        subject = Subject.objects.create(course=course, name='Subject1', staff=staff)
        response = self.client.get('/subjects/')
        self.assertContains(response, subject.name)
        self.assertContains(response, course.number)


class TestSubjectDetail(TestCase):
    def test_single_detail(self):
        self.client = Client()
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        course = Course.objects.create(number='1234', name='Test course')
        staff = Staff.objects.create(
            user=User.objects.create_user('test_staff', first_name='Staff')
        )
        subject = Subject.objects.create(course=course, name='Subject1', staff=staff)
        response = self.client.get(reverse('subject_detail', args=(subject.pk,)))
        self.assertContains(response, subject.name)
        self.assertContains(response, staff.name)
        self.assertEqual(response.status_code, 200)
