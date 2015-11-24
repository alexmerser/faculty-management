from django.contrib.auth.models import User
from django.db import models

from courses.models import Course


class Student(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=70, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    semester = models.PositiveIntegerField(default=1)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.user.get_full_name()


class Staff(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=35, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.user.get_full_name()
