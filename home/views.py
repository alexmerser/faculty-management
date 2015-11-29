from assignments.models import Assignment
from exams.models import Exam
from exams.views import ExamsList
from research.models import Research
from django.views.generic.base import TemplateView

from django import template
from django.contrib.auth.models import Group

class HomeView(TemplateView):
    template_name = 'home/home.html'
