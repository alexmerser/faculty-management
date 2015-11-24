from datetime import date

from django.db import models

from subjects.models import Subject
from users.models import Student


class Assignment(models.Model):
    subject = models.ForeignKey(Subject)
    topic = models.CharField(max_length=30)
    description = models.TextField()
    deadline = models.DateTimeField()
    tnow = date.today()


class AssignmentUpload(models.Model):
    subject = models.ForeignKey(Subject)
    topic = models.ForeignKey(Assignment)
    student = models.ForeignKey(Student)

    def __str__(self):
        return self.topic
