from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


def get_current_year():
    return timezone.now().year


class Course(models.Model):
    number = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=35, blank=True)
    description = models.TextField()
    year = models.PositiveIntegerField(default=get_current_year)
    semester = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.number


class Dean(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)

    def __str__(self):
        return 'Dean of ' + self.course.number
