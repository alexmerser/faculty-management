from django.views.generic import ListView

from courses.models import Dean
from users.models import Student, Staff


class StudentsList(ListView):
    model = Student


class StaffsList(ListView):
    model = Staff


class DeansList(ListView):
    model = Dean