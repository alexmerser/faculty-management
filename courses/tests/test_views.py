from datetime import date
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.test import TestCase

from courses.models import Course
from exams.models import Grade, Exam, ExamType
from subjects.models import Subject
from users.models import Student


class TestCourseDetail(TestCase):
    def test_empty(self):
        course = Course.objects.create(number='1234', name='Test course')
        response = self.client.get(reverse('course_detail', args=(course.pk,)))
        self.assertContains(response, course.number)
        self.assertContains(response, course.name)

    def test_one_student(self):
        course = Course.objects.create(number='1234', name='Test course')
        student = Student.objects.create(
            user=User.objects.create_user('test_user', first_name='Student'),
            course=course,
        )
        subject = Subject.objects.create(course=course, name='Subject1')
        exam_type = ExamType.objects.create(name='Final')
        exam = Exam.objects.create(exam_type=exam_type, subject=subject, hours=3, date=date(2015, 12, 12))
        grade = Grade.objects.create(exam=exam, student=student, value='A+')
        response = self.client.get(reverse('course_detail', args=(course.pk,)))
        self.assertContains(response, course.number)
        self.assertContains(response, course.name)
        self.assertContains(response, exam_type.name)
        self.assertContains(response, grade.value)
        self.assertContains(response, subject.name)
        self.assertContains(response, student.user.get_full_name())
