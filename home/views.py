from assignments.models import Assignment
from exams.models import Exam
from research.models import Research
from django.views.generic.base import TemplateView

from django import template
from django.contrib.auth.models import Group


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def researches(self):
        return Research.objects.order_by('submitted').reverse().all()

    def assignments(self):
        return Assignment.objects.order_by('deadline').reverse().all()

    def exams(self):
        return Exam.objects.order_by('date').reverse().all()
