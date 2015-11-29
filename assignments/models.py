from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from subjects.models import Subject


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

    def full_name(self):
        return self.user.get_full_name()


class AssignmentUpload(models.Model):
    assignment = models.ForeignKey(Assignment)
    user = models.ForeignKey(User)
    file = models.FileField(verbose_name='file', upload_to='uploads/')
    slug = models.SlugField(verbose_name='slug')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Upload to {} as {} at {}, {}'.format(
            self.assignment, self.user, self.created, self.file.name)
