from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.utils import timezone

from assignments.models import Assignment
from courses.models import Course
from subjects.models import Subject
from users.models import Student, Staff


class TestAssignmentList(TestCase):
    def test_single_assignment(self):
        self.client = Client()
        self.username = 'vba'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        course = Course.objects.create(number='1234', name='Test course')
        student = Student.objects.create(
            user=User.objects.create_user('test_user', first_name='Student'),
            course=course,
        )
        staff = Staff.objects.create(
            user=User.objects.create_user('test_staff', first_name='Staff')
        )
        subject = Subject.objects.create(course=course, name='Subject1', staff=staff)
        assignment = Assignment.objects.create(subject=subject, topic='This is Enemy', deadline=timezone.now())
        response = self.client.get('/assignments/')
        self.assertContains(response, assignment.topic)


class TestAssignmentDetail(TestCase):
    def test_one_student(self):
        self.client = Client()
        self.username = 'vba'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        course = Course.objects.create(number='1234', name='Test course')
        student = Student.objects.create(
            user=User.objects.create_user('test_user', first_name='Student'),
            course=course,
        )
        staff = Staff.objects.create(
            user=User.objects.create_user('test_staff', first_name='Staff')
        )
        subject = Subject.objects.create(course=course, name='Subject1', staff=staff)
        assignment = Assignment.objects.create(subject=subject, topic='This is Enemy', deadline=timezone.now(),
                                               description="I need holiday..")
        response = self.client.get(reverse('assignment_detail', args=(assignment.pk,)))
        self.assertContains(response, assignment.topic)
        self.assertContains(response, assignment.description)


class TestAssignmentUploadForm(TestCase):
    def upload_test(self):
        self.client = Client()
        self.username = 'vba'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)
        course = Course.objects.create(number='1234', name='Test course')
        student = Student.objects.create(
            user=User.objects.create_user('test_user', first_name='Student'),
            course=course,
        )
        staff = Staff.objects.create(
            user=User.objects.create_user('test_staff', first_name='Staff')
        )
        subject = Subject.objects.create(course=course, name='Subject1', staff=staff)
        assignment = Assignment.objects.create(subject=subject, topic='This is Enemy', deadline=timezone.now(),
                                               description="I need holiday..")
        with open('requirements.txt') as fp:
            self.client.post('/assignments/' + assignment.pk + '/upload/',
                             {'assignment': assignment, 'user': student.user, 'created': timezone.now(), 'file': fp})
        response = self.client.get(reverse('assignment_detail', args=(assignment.pk,)))
        print(response.status_code)
        self.assertContains(response, assignment.topic)
        self.assertContains(response, 'requirements.txt')
        self.assertEqual(response.status_code, 200)
