from django.views.generic import ListView, DetailView

from subjects.models import Subject


class SubjectList(ListView):
    model = Subject


class SubjectDetail(DetailView):
    model = Subject
