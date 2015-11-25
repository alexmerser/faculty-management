from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from courses.models import Course
from subjects.models import Subject


class SubjectList(ListView):
    model = Subject


class SubjectDetail(DetailView):
    model = Subject


