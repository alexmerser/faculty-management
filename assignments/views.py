from django.views.generic import ListView, DetailView

from assignments.models import Assignment


class AssignmentsList(ListView):
    model = Assignment


class AssignmentDetail(DetailView):
    model = Assignment