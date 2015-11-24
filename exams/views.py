from django.views.generic import DetailView, ListView

from exams.models import Exam


class ExamsList(ListView):
    model = Exam


class ExamDetail(DetailView):
    model = Exam