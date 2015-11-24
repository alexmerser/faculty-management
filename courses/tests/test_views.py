from datetime import date
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.test import TestCase

from courses.models import Course
from exams.models import Grade, Exam, ExamType
from subjects.models import Subject
from users.models import Student, Staff


class TestCourseList(TestCase):
    def test_single_subject(self):
        course = Course.objects.create(number="98765", name="Russian Language")
        response = self.client.get('/courses/')
        self.assertContains(response,course.number)
        self.assertContains(response,course.name)


class TestCourseDetail(TestCase):
    def test_empty(self):
        course = Course.objects.create(number='1234', name='Test course')
        #course = Course.objects.filter(name='')
        #course = Course.objects.get(name='')
        response = self.client.get(reverse('course_detail', args=(course.pk,)))
        self.assertContains(response, course.number)
        self.assertContains(response, course.name)

    def test_one_student(self):
        course = Course.objects.create(number='1234', name='Test course')
        student = Student.objects.create(
            user=User.objects.create_user('test_user', first_name='Student'),
            course=course,
        )
        staff = Staff.objects.create(
            user=User.objects.create_user('test_staff', first_name='Staff')
        )
        subject = Subject.objects.create(course=course, name='Subject1', staff=staff)
        response = self.client.get(reverse('course_detail', args=(course.pk,)))
        self.assertContains(response, course.number)
        self.assertContains(response, course.name)
        self.assertContains(response, subject.name)
        self.assertContains(response, student.user.get_full_name())


