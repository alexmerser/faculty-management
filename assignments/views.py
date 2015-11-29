from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from assignments.forms import AssignmentUploadForm
from assignments.models import Assignment, AssignmentUpload


class AssignmentsList(ListView):
    model = Assignment


class AssignmentDetail(DetailView):
    model = Assignment


class AssignmentUploadView(CreateView):
    model = AssignmentUpload
    form_class = AssignmentUploadForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs['user'] = user
        kwargs['assignment'] = get_object_or_404(Assignment, pk=self.kwargs['pk'])
        return kwargs

    def get_success_url(self):
        return reverse('assignment_detail', args=(self.object.assignment.pk,))
