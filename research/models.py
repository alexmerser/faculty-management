from datetime import date

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


class ResearchUpload(models.Model):
    # research = models.ForeignKey(Research)
    user = models.ForeignKey(Student)  # TODO: rename this to student
    subject = models.ForeignKey(Subject)  # TODO: delete this
    submitted = date.today()
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return 'Your file has been uploaded ! ' + self.subject.name
