from django.db import models

from subjects.models import Subject
from users.models import Student


class Research(models.Model):
    subject = models.ForeignKey(Subject)
    topic = models.CharField(max_length=30)
    submitted = models.DateTimeField()
    presented = models.DateTimeField()
    review = models.TextField()

    class Meta:
        verbose_name_plural = 'Researches'

    def __str__(self):
        return self.topic
