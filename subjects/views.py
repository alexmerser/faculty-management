from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from courses.models import Course
from subjects.models import Subject


class SubjectList(ListView):
    model = Subject


class SubjectDetail(DetailView):
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for student in self.object.student_set.all():
            students = []
            students = student.name_set.order_by('subject')
        for subject in self.object.subject_set.all():
            subjects = []
            subjects = subject.name_set.order_by('course')
        for research in self.object.research_set.all():
            researches = []
            researches = research.subject_set.order_by('date')
        for assignment in self.object.assignment_set.all():
            assignments = []
            assignments = assignment.subject_set.order_by('date')
            subjects.append(dict(
                pk=subject.pk,
                name=research.name,
                rdate=research.date,
                assignment=assignment.name,
                students=students,
            ))
        context['subjects'] = subjects
        print(subjects)
        print(students)
        print(researches)
        print(assignments)
        return context
