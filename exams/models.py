from django.db import models
from django.utils import timezone

from subjects.models import Subject
from users.models import Student


class ExamType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Exam(models.Model):
    exam_type = models.ForeignKey(ExamType)
    subject = models.ForeignKey(Subject)
    hours = models.PositiveIntegerField()
    date = models.DateTimeField()

    class Meta:
        unique_together = ("exam_type", "subject", "date")

    def __str__(self):
        return '{} in {} on {}'.format(self.exam_type, self.subject, self.date)

    @property
    def is_upcoming(self):
        return self.date > timezone.now()

class Grade(models.Model):
    exam = models.ForeignKey(Exam)
    student = models.ForeignKey(Student)
    VALUE_CHOICES = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F')
    )
    value = models.CharField(max_length=2, choices=VALUE_CHOICES)

    def __str__(self):
        return '{} {} {}'.format(self.student, self.exam, self.value)

    @property
    def return_username(self):
        return self.student.user