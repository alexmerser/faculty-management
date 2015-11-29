from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone

from courses.models import Course
from exams.models import ExamType, Exam, Grade
from subjects.models import Subject
from users.models import Student, Staff


class TestExamList(TestCase):
    def test_single_exam(self):
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
        exam_type = ExamType.objects.create(name="Final Exam")
        exam = Exam.objects.create(exam_type=exam_type, subject=subject, hours="2", date=timezone.now())
        response = self.client.get('/exams/')
        self.assertContains(response, exam.subject)
        self.assertEqual(response.status_code, 200)


class TestExamDetail(TestCase):
    def test_single_exam(self):
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
        exam_type = ExamType.objects.create(name="Final Exam")
        exam = Exam.objects.create(exam_type=exam_type, subject=subject, hours="2", date=timezone.now())
        student = Student.objects.create(
            user=User.objects.create_user('test_user', first_name='Student'),
            course=course,
        )
        grade = Grade.objects.create(exam=exam, student=student, value='A')
        response = self.client.get(reverse('exam_detail', args=(exam.pk,)))
        self.assertContains(response, exam.exam_type)
        self.assertContains(response, exam.subject)
        self.assertContains(response, exam.hours)
        self.assertContains(response, grade.value)
        self.assertEqual(response.status_code, 200)
