from django.db import models

from subjects.models import Subject


class Assignment(models.Model):
    subject = models.ForeignKey(Subject)
    topic = models.CharField(max_length=30)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.topic
