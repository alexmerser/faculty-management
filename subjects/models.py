from django.db import models

from courses.models import Course
from users.models import Staff


class Subject(models.Model):
    staff = models.ForeignKey(Staff)
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
