from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from subjects.models import Subject
from users.models import Student


class Assignment(models.Model):
    subject = models.ForeignKey(Subject)
    topic = models.CharField(max_length=30)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return '{} on {}'.format(self.topic, self.subject)

    @property
    def is_upcoming(self):
        return self.deadline > timezone.now()


class AssignmentUpload(models.Model):
    assignment = models.ForeignKey(Assignment)
    user = models.ForeignKey(User)
    file = models.FileField(upload_to='uploads/')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Upload to {} as {} at {}, {}'.format(
            self.assignment, self.user, self.created, self.file.name)
