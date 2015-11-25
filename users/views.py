from django.views.generic import ListView, DetailView
from courses.models import Dean
from users.models import Student, Staff


class StudentsDetail(DetailView):
    model = Student


class StaffsDetail(DetailView):
    model = Staff


class DeansDetail(DetailView):
    model = Dean